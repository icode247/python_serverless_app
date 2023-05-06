import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table_name = 'todos'


def create_item(event, context):
    req_body = json.loads(event['body'])
    try:
        table = dynamodb.Table(table_name)
        item = {
            'id': req_body['id'],
            'name': req_body['name']
        }
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': 'Item created successfully'
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }


def get_item(event, context):
    req_params = event['pathParameters']
    try:
        table = dynamodb.Table(table_name)
        item = table.get_item(Key={'id': req_params['id']})['Item']
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }


def update_item(event, context):
    req_params = event['pathParameters']
    req_body = json.loads(event['body'])

    try:
        table = dynamodb.Table(table_name)
        key = {'id': req_params['id']}
        update_expression = 'SET #n = :val1'
        expression_attribute_names = {'#n': 'name'}
        expression_attribute_values = {
            ':val1': req_body['name']}
        table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ExpressionAttributeValues=expression_attribute_values
        )
        return {
            'statusCode': 200,
            'body': 'Item updated successfully'
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }


def delete_item(event, context):
    req_params = event['pathParameters']
    try:
        table = dynamodb.Table(table_name)
        key = {'id': req_params['id']}
        table.delete_item(Key=key)
        return {
            'statusCode': 200,
            'body': 'Item deleted successfully'
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }


def handler(event, context):
    http_method = event['httpMethod']

    if http_method == 'POST':
        response = create_item(event, context)
    elif http_method == 'GET':
        response = get_item(event, context)
    elif http_method == 'PUT':
        response = update_item(event, context)
    elif http_method == 'DELETE':
        response = delete_item(event, context)
    else:
        response = {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid HTTP method'})
        }

    return response

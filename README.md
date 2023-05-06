# AWS Python Serverless Application

This repository contains a serverless web application built with Python and AWS Lambda. The application demonstrates a simple CRUD (Create, Read, Update, Delete) functionality using AWS Lambda functions and Amazon DynamoDB.

## Prerequisites
Before you can run this application, make sure you have the following installed:

- [Python 3.8](https://www.python.org/downloads/)
- [Node.js and npm](https://nodejs.org/en/download/)
- [AWS CLI](https://aws.amazon.com/cli/)
- [Serverless Framework](https://www.serverless.com/framework/docs/getting-started/)

Additionally, you need to have an AWS account and configure your AWS CLI with your credentials.

## Setup
Clone the repository:


      git clone https://github.com/icode247/python_serverless_app.git
      cd python_serverless_app
          
          
## Install the dependencies:


      pip install -r requirements.txt
          
## Deploy the application to AWS:

      sls deploy
          
This command will create the necessary AWS resources, such as Lambda functions and a DynamoDB table. Note the API endpoint displayed in the output after the deployment is complete.

## Running the Application

### Local Testing
To test the application locally, use the Serverless Offline plugin:

     sls offline
         
This command will start a local server on port `3000` by default. You can test your Lambda function by making a request to the local endpoint:


    curl http://localhost:3000/dev/items/{id}  
       
To stop the local server, press `Ctrl + C` in the terminal.

### Testing on AWS

After deployment, you can test the application using the API endpoint provided in the deployment output. Use the following command, replacing your-api-endpoint with the actual API endpoint:


    curl https://your-api-endpoint.amazonaws.com/dev/items/{id}
        
## Cleaning Up
To remove the deployed AWS resources, run the following command:


   sls remove
       
This will delete the Lambda functions, DynamoDB table, and other resources created during deployment.

## Contributing
Feel free to submit issues, fork the repository, and create pull requests to contribute to the project.

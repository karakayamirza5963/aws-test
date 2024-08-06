**AWS BASIC WEBSITE**

![Architecture](./aws%20website%20architecture.png)


**Purpose:** *Setting up a basic web app that counts how many people entered the site by using AWS.*

**Services i have used:** *Amplify, API Gateway, Lambda, IAM, DynamoDB.*

**HOW?:** 

*1- Create a DynamoDB database, add an item with a primary key and an attribute(Integer to count visits).*

*2- Create a Lambda function (Code given in repo), attach the database you created with DynamoDB to it.*

*3- Create an IAM policy for Lambda function (example in repo/IAM).*

*4- Create an API Gateway and attach Lambda function to it. (Don't forget to enable CORS).*

*5- Create an Amplify website (example website in repo/amplify), and edit it to send requests to your API Gateway endpoint.*

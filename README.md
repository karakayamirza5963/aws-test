*AWS BASIC WEBSITE*

![Architecture](https://private-user-images.githubusercontent.com/169092360/355388755-faf29bf0-4e94-4bd0-915a-0ff2df7d0761.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5MzU5NDMsIm5iZiI6MTcyMjkzNTY0MywicGF0aCI6Ii8xNjkwOTIzNjAvMzU1Mzg4NzU1LWZhZjI5YmYwLTRlOTQtNGJkMC05MTVhLTBmZjJkZjdkMDc2MS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgwNlQwOTE0MDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hYzlkN2RjYzI4YWM3NmM4YTIyYzJjMTVhYmQwOWUwYjExZDI5Y2VmZGFlNTJhYmU5YTZhNDg0NzhiYjRjMmI2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.s3yI5o4o9-xvcTqxeOdczgKeKzPxvZ96WNoiu1LOrv8)


**Purpose:** *Setting up a basic web app that counts how many people entered the site by using AWS.*

**Services i have used:** *Amplify, API Gateway, Lambda, IAM, DynamoDB.*

**HOW?:** 
*1- Create a DynamoDB database, add an item with a primary key and an attribute(Integer to count visits).*
*2- Create a Lambda function (Code given in repo), attach the database you created with DynamoDB to it.*
*3- Create an IAM policy for Lambda function (example in repo/IAM).*
*4- Create an API Gateway and attach Lambda function to it. (Don't forget to enable CORS).*
*5- Create an Amplify website (example website in repo/amplify), and edit it to send requests to you API Gateway endpoint.*

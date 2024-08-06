import json
import boto3

#'hmTimes' here is the table attribute on my dynamodb table, you can change it if you set up the variable with different name.

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TableName") #Your dynamodb table name.
def lambda_handler(event, context):

    response = table.update_item(
        Key={'ID': 1}, #'ID' might change if you set up the primary key with a different name on dynamodb, so don't forget to set it up right.
        UpdateExpression="set hmTimes = hmTimes + :val",
        ExpressionAttributeValues={':val': 1},
        ReturnValues="UPDATED_NEW"
    )
    

    updated_value = int(response['Attributes']['hmTimes'])
    return {
        'statusCode': 200,
        'body': json.dumps({'amounts': updated_value})
    }
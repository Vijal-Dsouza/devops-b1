import json
import boto3

client = boto3.client('dynamodb')


def lambda_handler(event, context):
    
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        response = client.put_item(
            TableName='devops-b1',
            Item={
                'Emp_Id': {'S': body.get('Emp_Id')},
                'First_Name': {'S': body.get('First_Name')},
                'Last_Name': {'S': body.get('Last_Name')},
                'Joining_Date': {'S': body.get('Joining_Date')}
            }
        )
    else: 
        print(event)
        Emp_Id = event['queryStringParameters']['Emp_Id']
        response = client.get_item(
            TableName='devops-b1',
            Key={
                'Emp_Id': {'S': Emp_Id}
            }
        )

    return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": response})
        }
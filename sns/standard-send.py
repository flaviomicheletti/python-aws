import boto3
import json
import config

sns = boto3.client(
    'sns',
    region_name=config.region,
    aws_access_key_id=config.access,
    aws_secret_access_key=config.secret
)

topic_arn = 'arn:aws:sns:us-east-1:659014245856:TestTopic'
message = {"foo": "bar"}

response = sns.publish(
    TopicArn=topic_arn,
    Message=json.dumps(message),
    Subject='Test SNS message',
    MessageAttributes={"TransactionType": {"DataType": "String", "StringValue": "Order"}}
)

print(response['ResponseMetadata']['HTTPStatusCode'])

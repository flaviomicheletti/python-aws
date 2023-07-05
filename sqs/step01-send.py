import boto3
import config

sqs = boto3.client(
    config.type,
    region_name=config.region,
    aws_access_key_id=config.access,
    aws_secret_access_key=config.secret
)

queue_url = config.queue_url

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Hello, SQS!'
)

print(response['MessageId'])

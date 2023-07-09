import boto3
import config

sqs = boto3.client(
    'sqs',
    region_name=config.region,
    aws_access_key_id=config.access,
    aws_secret_access_key=config.secret
)

queue_url = config.queue_url

# Receive and delete messages until the queue is empty
while True:
    # Receive messages from the queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10  # Adjust the number of messages to receive at once
    )

    # Check if there are any messages
    messages = response.get('Messages', [])
    if not messages:
        break  # Exit the loop if no messages are returned

    # Process each message
    for message in messages:
        # Do something with the message data
        print('Received message:', message['Body'])


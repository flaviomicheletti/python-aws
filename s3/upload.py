import boto3
import botocore.exceptions
import random

local_file_path = 's3/file.txt'
bucket_name = 'flavio-s3'

random_number = random.randint(1000, 9999)
object_key = f'file-{str(random_number)}.txt'

try:
    s3 = boto3.client('s3')
    s3.upload_file(local_file_path, bucket_name, object_key)
    print(f"File {local_file_path} uploaded successfully to bucket {bucket_name}.")
except botocore.exceptions.ClientError as e:
    print(f"Error uploading file: {e.response['Error']['Message']}")

    
# File s3/file.txt uploaded successfully to bucket flavio-s3.
import boto3

bucket_name = 'flavio-s3'

object_key = 'file-3096.txt'

local_file_path = 's3/file-3096.txt'

s3 = boto3.client('s3')

try:
    s3.download_file(bucket_name, object_key, local_file_path)
    print(f"File '{object_key}' has been downloaded from bucket '{bucket_name}' to '{local_file_path}'.")
except Exception as e:
    print(f"Error downloading file: {e}")
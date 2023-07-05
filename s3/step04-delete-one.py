import boto3

bucket_name = 'flavio-s3'
object_key = 'file-4703.txt'

s3 = boto3.client('s3')

try:
    response = s3.delete_object(Bucket=bucket_name, Key=object_key)
    print(f"File '{object_key}' has been deleted from bucket '{bucket_name}'.")
except Exception as e:
    print(f"Error deleting file: {e}")
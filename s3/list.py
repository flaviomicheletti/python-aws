import boto3

bucket_name = 'flavio-s3'
s3 = boto3.client('s3')

try:
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Check if the response contains any objects
    if 'Contents' in response:
        print(f"Files in bucket '{bucket_name}':")
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print(f"No files found in bucket '{bucket_name}'.")
except Exception as e:
    print(f"Error listing objects in bucket: {e}")

# Files in bucket 'flavio-s3':
# file-2485.txt
# file-3737.txt
# file-6580.txt

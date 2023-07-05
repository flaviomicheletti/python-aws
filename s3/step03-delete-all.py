import boto3

bucket_name = 'flavio-s3'

s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)

try:
    response = bucket.objects.all().delete()
    print(f"All files in bucket '{bucket_name}' have been deleted.")
except Exception as e:
    print(f"Error deleting objects in bucket: {e}")

import boto3

client = boto3.client('elasticache')

response = client.delete_cache_cluster(CacheClusterId='my-cluster')
print(response)

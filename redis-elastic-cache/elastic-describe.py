import boto3


client = boto3.client('elasticache')


response = client.describe_cache_clusters()
clusters = response['CacheClusters']
for cluster in clusters:
    print(cluster['CacheClusterId'])

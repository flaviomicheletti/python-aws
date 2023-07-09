import boto3

client = boto3.client('elasticache')

response = client.create_cache_cluster(
    CacheClusterId='my-cluster',
    CacheNodeType='cache.t2.micro',
    Engine='redis',
    NumCacheNodes=1
    )
print(response)


"""
{
   "CacheCluster":{
      "CacheClusterId":"my-cluster",
      "ClientDownloadLandingPage":"https://console.aws.amazon.com/elasticache/home#client-download:",
      "CacheNodeType":"cache.t2.micro",
      "Engine":"redis",
      "EngineVersion":"7.0.7",
      "CacheClusterStatus":"creating",
      "NumCacheNodes":1,
      "PreferredMaintenanceWindow":"thu:04:00-thu:05:00",
      "PendingModifiedValues":{
         
      },
      "CacheSecurityGroups":[
         
      ],
      "CacheParameterGroup":{
         "CacheParameterGroupName":"default.redis7",
         "ParameterApplyStatus":"in-sync",
         "CacheNodeIdsToReboot":[
            
         ]
      },
      "CacheSubnetGroupName":"default",
      "AutoMinorVersionUpgrade":true,
      "SnapshotRetentionLimit":0,
      "SnapshotWindow":"09:30-10:30",
      "TransitEncryptionEnabled":false,
      "AtRestEncryptionEnabled":false,
      "ARN":"arn:aws:elasticache:us-east-1:659014245856:cluster:my-cluster",
      "ReplicationGroupLogDeliveryEnabled":false,
      "LogDeliveryConfigurations":[
         
      ],
      "NetworkType":"ipv4",
      "IpDiscovery":"ipv4"
   },
   "ResponseMetadata":{
      "RequestId":"3c1a1fd8-b27c-459f-b8b0-1e1a7adc98c5",
      "HTTPStatusCode":200,
      "HTTPHeaders":{
         "x-amzn-requestid":"3c1a1fd8-b27c-459f-b8b0-1e1a7adc98c5",
         "content-type":"text/xml",
         "content-length":"1764",
         "date":"Sun, 09 Jul 2023 14:47:07 GMT"
      },
      "RetryAttempts":0
   }
}
"""
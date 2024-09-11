import boto3

# Set up Boto3 client with retrieved credentials and region
eks_client = boto3.client(
    'eks',
    aws_access_key_id=<access_key>,
    aws_secret_access_key=<secret_access>,
    region_name='<region>'
)

# List ready or healthy EKS clusters in the specified AWS region
try:
    eks_clusters = eks_client.list_clusters()
    print("Ready or Healthy EKS Clusters:")
    for cluster_name in eks_clusters['clusters']:
        cluster_info = eks_client.describe_cluster(name=cluster_name)
        if cluster_info['cluster']['status'] == 'ACTIVE':
            print(f" - EKS Cluster: {cluster_name}")
except Exception as e:
    print(f"Error listing ready or healthy clusters: {str(e)}")

"""
Simple EC2 Manager CLI (boto3)
Prereqs:
 - pip install boto3
 - Configure AWS credentials (aws configure) or env vars
 - IAM permissions for S3 actions
"""

# export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
# export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
# export AWS_DEFAULT_REGION="ap-south-1"

import boto3

client = boto3.client('s3')

# Listing Buckets
response = client.list_buckets()
print(response)

try:
    response = client.create_bucket(
    Bucket='python-2522-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2',
    },
)
    print("Bucket Creation Status: ",response)
except Exception as e:
    print("Error creating bucket:", e)

# NEWLY ADDED    
# Deleting Buckets
response = client.delete_bucket(
    Bucket='python-2522-bucket',
)
print(response)
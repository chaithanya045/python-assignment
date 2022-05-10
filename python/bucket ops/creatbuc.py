from urllib import response
import boto3
s3_client=boto3.client('s3')
bucket_name=str(input('enter your bucket name:'))
response=s3_client.create_bucket(
    ACL='private',
    Bucket=bucket_name
)
print(response)

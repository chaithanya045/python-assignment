import boto3
client=boto3.client('s3')
bucket_name=str(input('enter your buck name'))
buck_create=client.create_bucket(
    ACL='private',
    Bucket=bucket_name
)

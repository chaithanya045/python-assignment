import boto3
import os

client=boto3.client('s3')

for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'my-pyth-bucket235'
        upload_file_key =  "python/"+str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
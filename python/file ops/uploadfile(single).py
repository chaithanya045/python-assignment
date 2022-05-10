import boto3
s3=boto3.client('s3')
s3.upload_file('trans.txt','my-pyth-bucket235','s4_changed')
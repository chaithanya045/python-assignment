import boto3
s3 = boto3.client('s3')
bucket_name = "my-pyth-bucket235"
directory_name = "python123" #it's name of your folders
s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
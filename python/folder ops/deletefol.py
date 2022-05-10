import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('my-pyth-bucket235')
bucket.objects.filter(Prefix="python123/").delete()
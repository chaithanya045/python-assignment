import boto3
s3=boto3.resource('s3')

copy_source = {
    'Bucket': 'myfirstone2022',
    'Key': 'basic.py'
}

bucket = s3.Bucket('my-pyth-bucket235')

bucket.copy(copy_source, 'basic.py')
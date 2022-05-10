import boto3

client = boto3.client('s3')
client.delete_object(Bucket='my-pyth-bucket235', Key='part2.py')
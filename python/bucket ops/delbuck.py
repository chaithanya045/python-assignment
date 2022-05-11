
import boto3
client=boto3.client('s3')
bucket=str(input("enter the bucket name that you want to delete : ")
response=client.list_buckets()
for n in response['Buckets']:
    print(n['Name'])

client.delete_bucket(
    Bucket=bucket
)
print('after deleting the bucket the remaining bucket are:')
response=client.list_buckets()
for n in response['Buckets']:
    print(n['Name'])


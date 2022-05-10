import boto3
client=boto3.client('s3')
bucket='my-pyth-bucket235'
all_objects=client.list_objects(Bucket=bucket)
print(f"list in {bucket}:")
for a in all_objects["Contents"]:
    print(a["Key"])
def del_file(filename):
    client.delete_object(Bucket=bucket,Key=filename)
for a in all_objects["Contents"]:
    if ".py" in a["Key"]:
        del_file(a["Key"])
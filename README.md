# python-assignment

1)**for listing the contents of the file**

import boto3                         (#imported the boto3 module for connecting to s3)
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():      (#for printing all the bucketnames in my s3 )
  print(bucket.name)
  
  
2)**File operations(Uploading,deleting the files)**
**a)for uploading the files**
import boto3
import os   (#imported the os module for connecting to os)
client=boto3.client('s3')                                            (#connecting the client to s3)
for file in os.listdir():
    if '.py' in file:                                                (# for uploading the python files that i have created)
        upload_file_bucket = 'my-pyth-bucket235'                     (#the bucket name that we have to upload the files)
        upload_file_key =  "python/"+str(file)                       (#creating the folder in the bucket to dump the all python files into that folder)
        client.upload_file(file, upload_file_bucket, upload_file_key) (#upload_file method is used to upload the required files) 
        
     
**b)for deleting the files **

import boto3
client=boto3.client('s3')
bucket='my-pyth-bucket235'                            (#the bucket name that we have to delete the files)
all_objects=client.list_objects(Bucket=bucket)
print(f"list in {bucket}:")
for a in all_objects["Contents"]:                     (#for printing the all files in bucket before deleting it)
    print(a["Key"])
def del_file(filename):
    client.delete_object(Bucket=bucket,Key=filename)   (#dele_object method is used to deleting the required files)
for a in all_objects["Contents"]:                       
    if ".py" in a["Key"]:                              (#deleting the all files that contains ".py" extension)
        del_file(a["Key"])
        
  
**3)Bucket operations(creating and deleting the bucket)
a)creating the bucket**
import boto3
client=boto3.client('s3')
bucket_name=str(input('enter your buck name'))
buck_create=client.create_bucket(                     (#create_bucket method is used for creating the bucket)
    ACL='private',                                    (# access control list for making private)
    Bucket=bucket_name
)


**b)deleting the bucket**
import boto3
client=boto3.client('s3')
bucket=str(input('enter your bucket name that you want to delete:")
response=client.list_buckets()
for n in response['Buckets']:                                (#to list all the buckets before deleting the required buckets)
    print(n['Name'])

client.delete_bucket(                                         (#dele_object method is used to deleting the required buckets)
    Bucket=bucket
)
print('after deleting the bucket the remaining bucket are:')   (#to list all the buckets after deleting the required buckets)
response=client.list_buckets()
for n in response['Buckets']:
    print(n['Name'])
    
4)Folder operations
   


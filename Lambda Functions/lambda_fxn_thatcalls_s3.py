import boto3    #import boto3 SDK library
import os

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')  #create s3 client via SDK

    bucket = os.environ['BUCKET_NAME'] #bucket name configured in environment variable

    response = s3.list_objects(Bucket = bucket)   #RUN SDK Api call to retrieve list of objects

    object_list = [content['Key'] for content in response.get('Contents', [])] #list object keys(names) 4m response

    return object_list #return list as an output of the function
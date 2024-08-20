import boto3 #import the boto3 SDK library
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb') #create dynamodb client via SDK

    table_name = os.environ['TABLE_NAME'] #table name configured in an environment variable

    table = dynamodb.Table(table_name) #create table object via SDK

    pkey = {'username': 'makit'} #define parttion key being retrieved

    response = table.get_item(Key=pkey)

    item = response.get('Item') #read the full item from the response and then return

    return item
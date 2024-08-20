import boto3 #Import boto library(SDK)

def lambda_handler(event, context):

    client = boto3.client(service_name='ssm') #Create Systems Manager client

    #SDK call to get parameter and ask for it to be decrypted
    #Note that here execution role needs perm to retrieve value & decrypt value with KMS
    get_parameter_response = client.get_parameter(Name='my-password', WithDecryption=True)

    #Read decrypted parameter value from the response
    password = get_parameter_response['Parameter']['Value']

    return password[:2]#Do some secret thing with password #show first two characters
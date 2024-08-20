import boto3 #import boto library(SDK)

def lambda_handler(event, context):
    client = boto3.client(service_name='secretsmanager') #Create secrets manager client

    get_secret_value_response = client.get_secret_value(SecretID='my-password') #SDK call to get secret
    #execution role of the function will need permission to get secret

    password = get_secret_value_response['SecretString'] #read secret from response


    return password[:2]
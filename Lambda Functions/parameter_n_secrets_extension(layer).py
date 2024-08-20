#Parameter and Secrets Extension is distr as layer
#Once the layer exists, then the Lambda function can use it like this
#Integrated using http requests


import json, os, urllib3 #import dependencies

def lambda_handler(event, context):

    #Read session token to pass to the extension so it can use execution role(of fxn)
    #Token provided by the runtime as an environment variable
    aws_session_token = os.environ['AWS_SESSION_TOKEN']

    #code will need to make http request to the extension which is running within environment
    #Will call extension running on port 2773(port for the local HTTP server)
    url = ('http://localhost:2773/secretsmanager/get?secretId=my-password')

    headers = { "X-Aws-Parameters-SecretsToken": aws_session_token}

    #GET request to the extension
    response = urllib3.PoolManager().request("GET", url, headers=headers)

    response = json.loads(response.data)#Data returned as JSON

    return response['SecretString'][:2]

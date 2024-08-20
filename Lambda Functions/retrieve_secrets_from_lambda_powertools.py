#Can be installed as a layer or as a dependency
#simple way to access secrets compared to Param & Secrets Extension and Systems Manager Parameter Store(feature of Systems Manager service) 


from typing import Any
from aws_lambda_powertools.utilities import parameters #import dependencies

def lambda_handler(event, context):


    #use utility to retrieve secret passing on age param to specify how long to cache it for
    #Read the secret given the secret name and a cache TTL
    password: Any = parameters.get_secret("my-password", max_age=10)

    return password[:2]
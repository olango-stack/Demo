#event object
#object has two properties x, y
#returns result in a http style object



import json
def lambda_handler(event, context):
    x = event['x']
    y = event['y']

    result = x * y

    print(f"Multiplication result: {result}")

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
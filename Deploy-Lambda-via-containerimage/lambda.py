def handler(event, context):
    result = event['x'] * event['y']
    print(result)
    return {'result': result}
import boto3
import os
import json


def lambda_handler(event, context):
    eventbridge = boto3.client('events')

    my_event = json.dumps({'orderValue': 259, 'customerName': 'jeff'})

    response = eventbridge.put_events(
        Entries=[{
            'EventBusName': 'businessbus',
            'Source': 'business.website',
            'DetailType': 'Order Placed',
            'Detail': my_event
        }]
    )

    return response['Entries'][0]
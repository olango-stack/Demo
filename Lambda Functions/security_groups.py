import boto3
import hashlib
import json
import urllib3

http = urllib3.PoolManager()

# Name of the service, as seen in the ip-groups.json file to extract information for

SERVICE = "CLOUDFRONT"

# Ports your application uses that need inbound permissions from the service for
INGRESS_PORTS = {'Http': 80}
# Tags which identify the security groups you want to update
SECURITY_GROUP_TAG_FOR_GLOBAL_HTTP = {'Name': 'cloudfront_g', 'AutoUpdate': 'true', 'Protocol': 'http'}
SECURITY_GROUP_TAG_FOR_REGION_HTTP = {'Name': 'cloudfront_r', 'AutoUpdate': 'true', 'Protocol': 'http'}


SG_RULES_LIMIT = 60

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    message  = json.loads(event['Records'][0]['Sns']['Message'])
    
    #Load the ip ranges from the url
    ip_ranges = json.loads(get_ip_groups_json(message['url'], message['md5']))
    
    #extract the service ranges
    
    global_cf_ranges = get_ranges_for_service(ip_ranges, SERVICE, "GLOBAL")
    region_cf_ranges = get_ranges_for_service(ip_ranges, SERVICE, "REGION")
    
    #split global ip list if more than soft limit
    if (len(global_cf_ranges)) > SG_RULES_LIMIT:
        global_cf_ranges_1 = (global_cf_ranges[:SG_RULES_LIMIT])
        global_cf_ranges_2 = (global_cf_ranges[SG_RULES_LIMIT:])
        global_cf_ranges = [global_cf_ranges_1, global_cf_ranges_2]
        
    #limit regional ip list if more than soft limit
    if (len(region_cf_ranges)) > SG_RULES_LIMIT:
        region_cf_ranges = (region_cf_ranges[:SG_RULES_LIMIT])
        
    ip_ranges = {"GLOBAL": global_cf_ranges, "REGION": region_cf_ranges}
    
    result = update_security_groups(ip_ranges)
    return result


def get_ip_groups_json(url, expected_hash):
    print("Updating from " + url)
    response = http.request('GET', url)
    ip_json = response.data
    
    return ip_json

def get_ranges_for_service(ranges, service, subset):
    service_ranges = list()
    for  prefix in ranges['prefixes']:
        if prefix['service'] == service and ((subset == prefix['region'] and subset == "GLOBAL") or (subset != 'GLOBAL' and prefix['region'] != 'GLOBAL')):
            print('Found' + service + ' region: ' + prefix['region'] + ' range: ' + prefix['ip_prefix'])
            service_ranges.append(prefix['ip_prefix'])
            
    return service_ranges
    
def update_security_groups(new_ranges):
    client = boto3.client('ec2')
    
    
    global_http_group = get_security_groups_for_update(client, SECURITY_GROUP_TAG_FOR_GLOBAL_HTTP)
#!/usr/bin/python
import time
import boto3, sys
from botocore.client import Config

#bucket_name = sys.argv[1]
#obj_prefix = sys.argv[2]

ENDPOINT_URL = 'http://10.206.176.34/'
ACCESS_KEY = 'SDmbB1ZpBT1pSYDyfeQv'
SECRET_KEY = 'XKKWGChrPASmvjOVCORzKwz2Ra6UGJ9aSisW0xsu'
BUCKET_NAME = 'test0008'

def show_resp(response):
    print '>>>>>>>>>>>>>>>>> show response:'
    #print response['ResponseMetadata']
    #print response['Contents']
    for k in response.keys():
        print k, ":",
        if k == 'Contents':
            print ""
            for i in response['Contents']:
                print i
        else:
            print response[k]
    print ""


s3_cli = boto3.client('s3', 'us-west-1',
    config=Config(signature_version='s3v4'), use_ssl=False,
    endpoint_url=ENDPOINT_URL,
    aws_secret_access_key=SECRET_KEY,
    aws_access_key_id=ACCESS_KEY)

#start=time.time()
#response = s3_cli.list_objects(
#    Bucket=BUCKET_NAME,
#    MaxKeys=3
#)
#end=time.time()
#print(end-start)

response = s3_cli.list_objects_v2(
    Bucket=BUCKET_NAME,
    Delimiter='/',
    MaxKeys=3
)
show_resp(response)
is_truncated = response['IsTruncated']
next_token = response['NextContinuationToken']

if is_truncated is True:
    response = s3_cli.list_objects_v2(
        Bucket=BUCKET_NAME,
        Delimiter='/',
        ContinuationToken=next_token,
        #MaxKeys=10
    )
    show_resp(response)



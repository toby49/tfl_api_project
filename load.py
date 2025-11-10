import os #find .env file
import sys
import boto3 #s3 bucket
from dotenv import load_dotenv #load variables from .env

load_dotenv() #load variables from .env

aws_access_key = os.getenv('aws-access-key')
aws_secret_key = os.getenv('aws-bikepoint-access-key-secret')
bucket = os.getenv('bucket')

s3_client = boto3.client(
    's3'
    , aws_access_key_id = aws_access_key
    , aws_secret_access_key = aws_secret_key
)

try: 
    try:
        print(s3_client.list_objects_v2(Bucket=bucket)) # Test if connection is successful
    except:
        print('Access denied')
        sys.exit(1)
    
    # If so, run this code:
    dir = 'data'
    file = [f for f in os.listdir(dir) if f.endswith('.json')]

    if len(file)>0: # Test if there are any files to upload
        filename = dir + '/' + file[0]
        s3filename = file[0]
        s3_client.upload_file(filename, bucket, s3filename)
        os.remove(filename)
    else:
        print('No files to upload')

except Exception as e: 
    print(e)
    raise e


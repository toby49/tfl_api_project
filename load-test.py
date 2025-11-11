import os #find .env file
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

filename = 'data/2025-11-05T15-24-58.json'
s3filename = '2025-11-05T15-24-58.json'

s3_client.upload_file(filename, bucket, s3filename)

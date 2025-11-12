import os
from extract import extract
from load import load
import sys
import boto3 #s3 bucket
from dotenv import load_dotenv #load variables from .env
import requests as r
import time
import json
from datetime import datetime

url = 'https://api.tfl.gov.uk/BikePoint/'
print('running extract')
extract(url)
print('extract done')


print('starting load')

load()

print('load done')
import requests as r
import time
from datetime import datetime

url = 'https://api.tfl.gov.uk/BikePoint/'

response = r.get(url, timeout=10)

print(response.status_code)




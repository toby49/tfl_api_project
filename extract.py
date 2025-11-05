import requests as r
import time
import json
from datetime import datetime

# API documentation: https://api-portal.tfl.gov.uk/api-details#api=BikePoint
# Base endpoint to retrieve all Santander Cycle hire BikePoints
url = 'https://api.tfl.gov.uk/BikePoint/'

# Make initial API request to TfL
response = r.get(url, timeout=10)

# Retry if API rate limits (429) or returns internal server error (500)
retry_codes = [429,500] # retry if 429: too many requests, or 500: connectivity issues

# Define variables for testing number of API calls
count = 0 
max_tries = 3  # safety limit to avoid infinite requests

while count < max_tries:
    if response.status_code == 200: # if call is successful
        try: # when API is successful, check that response is JSON format
            data = response.json()  # parse API JSON response
        except Exception as e:
            print(e) # print error if response isn't valid JSON
            break
        
        extract_timestamp = datetime.now() # record time of extraction

        # Append extract timestamp to each bikepoint in response dictionary.
        # Useful for tracking when data was collected
        for bp in data: 
            bp['extract_timestamp'] = str(extract_timestamp)

        # Save file with timestamp-based filename to avoid overwriting
        filepath = 'data/' + extract_timestamp.strftime('%Y-%m-%dT%H-%M-%S') + '.json'

        # Write data to file in JSON format
        with open(filepath,'w') as file:
            json.dump(data,file)
        break

    elif response.status_code in retry_codes:
        time.sleep(10)  # wait before retry to avoid hammering API
        print(response.reason())  # print reason (e.g., Too Many Requests)
        count+=1  # increment retry count

    else:
        # Any other response (e.g. 400/404) breaks script
        print(response.reason())
        break

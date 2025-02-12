import json
import os

import requests


def fetch_apod():
    print('Fetching the Astronomy Picture of the Day...')
    _API_KEY = os.getenv('NASA_API_KEY')
    _API_URL = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': _API_KEY
    }
    request = requests.get(_API_URL, params=params)
    print(json.dumps(request.json(), indent=4))


if __name__ == '__main__':
    # Fetch the Astronomy Picture of the Day
    fetch_apod()

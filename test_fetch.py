# Test Fetch APOD
from io import StringIO
import os
from unittest.mock import patch, create_autospec

import requests

from fetch_apod import fetch_apod


@patch('fetch_apod.os.getenv', spec=os.getenv)
@patch('fetch_apod.requests.get', spec=requests.get)
@patch('sys.stdout', new_callable=StringIO)
def test_fetch(stdout_mock, get_mock, getenv_mock):
    get_mock.return_value.json.return_value = {'star': 'stuff'}
    get_mock.return_value.status_code = 200
    getenv_mock.return_value = '12345'
    fetch_apod()
    getenv_mock.assert_called_once_with('NASA_API_KEY')
    get_mock.assert_called_once_with('https://api.nasa.gov/planetary/apod', params={'api_key': '12345'})
    out_val = stdout_mock.getvalue()
    assert out_val == os.linesep.join([
    'Fetching the Astronomy Picture of the Day...',
    '{',
    '    "star": "stuff"',
    '}',
    ''])

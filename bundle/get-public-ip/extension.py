#!/usr/bin/env python3
import json
import os
import requests
import signal
import sys
from pathlib import Path
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

LAMBDA_EXTENSION_NAME = Path(__file__).parent.name

def execute_custom_processing(event):
    retry_strategy = Retry(
        total = 3,
        status_forcelist = [429, 500, 502, 503, 504],
        backoff_factor = 1
    )
    adapter = HTTPAdapter(
        max_retries = retry_strategy
    )
    http = requests.Session()
    http.mount("https://", adapter)
    r = http.get('https://checkip.amazonaws.com')
    print(f"[{LAMBDA_EXTENSION_NAME}] {r.text}", flush=True)

def handle_signal(signal, frame):
    sys.exit(0)

def register_extension():
    headers = {
        'Lambda-Extension-Name': LAMBDA_EXTENSION_NAME,
    }
    payload = {
        'events': [
            'INVOKE',
            'SHUTDOWN'
        ],
    }
    response = requests.post(
        url=f"http://{os.environ['AWS_LAMBDA_RUNTIME_API']}/2020-01-01/extension/register",
        json=payload,
        headers=headers
    )
    ext_id = response.headers['Lambda-Extension-Identifier']
    return ext_id

def process_events(ext_id):
    headers = {
        'Lambda-Extension-Identifier': ext_id
    }
    while True:
        response = requests.get(
            url=f"http://{os.environ['AWS_LAMBDA_RUNTIME_API']}/2020-01-01/extension/event/next",
            headers=headers,
            timeout=None
        )
        event = json.loads(response.text)
        if event['eventType'] == 'SHUTDOWN':
            sys.exit(0)
        else:
            execute_custom_processing(event)

def main():

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    extension_id = register_extension()
    process_events(extension_id)

if __name__ == "__main__":
    main()
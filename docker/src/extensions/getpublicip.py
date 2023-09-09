#!/bin/sh
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

''''exec python -u -- "$0" ${1+"$@"} # '''
import os
import sys
from pathlib import Path
from datetime import datetime
 
lib_folder = Path(__file__).parent / "lib"
sys.path.insert(0,str(lib_folder))

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from getpublicip.extensions_api_client import ExtensionsAPIClient

class GetPublicIP():

    def __init__(self, agent_name, registration_body):

        self.agent_name = agent_name
        self.extensions_api_client = ExtensionsAPIClient()
        self.agent_id = self.extensions_api_client.register(self.agent_name, registration_body)

    def run_forever(self):

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

        publicip = r.text.strip()
        now = datetime.now()

        try:
            awsaccount = os.environ['AWS_ACCOUNT']
        except:
            awsaccount = 'Please add the AWS_ACCOUNT environment variable to the Lambda.'
            pass

        output = {
            "publicip": publicip,
            "timestamp": now.strftime("%m/%d/%Y %H:%M:%S.%f UTC"),
            "function": os.environ['AWS_LAMBDA_FUNCTION_NAME'],
            "region": os.environ['AWS_REGION'],
            "account": awsaccount
        }

        print(f"{str(output)}", flush=True)

        while True:
            resp = self.extensions_api_client.next(self.agent_id)

_REGISTRATION_BODY = {
    "events": ["INVOKE", "SHUTDOWN"],
}

def main():

    ext = GetPublicIP(os.path.basename(__file__), _REGISTRATION_BODY)
    ext.run_forever()

if __name__ == "__main__":
    main()

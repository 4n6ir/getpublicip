# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import os
import sys
import urllib.request

LAMBDA_AGENT_NAME_HEADER_KEY = "Lambda-Extension-Name"
LAMBDA_AGENT_IDENTIFIER_HEADER_KEY = "Lambda-Extension-Identifier"

class ExtensionsAPIClient():

    def __init__(self):

        try:
            runtime_api_address = os.environ['AWS_LAMBDA_RUNTIME_API']
            self.runtime_api_base_url = f"http://{runtime_api_address}/2020-01-01/extension"
        except Exception as e:
            raise Exception(f"AWS_LAMBDA_RUNTIME_API is not set {e}") from e

    def register(self, agent_unique_name, registration_body):

        try:
            req = urllib.request.Request(f"{self.runtime_api_base_url}/register")
            req.method = 'POST'
            req.add_header(LAMBDA_AGENT_NAME_HEADER_KEY, agent_unique_name)
            req.add_header("Content-Type", "application/json")
            data = json.dumps(registration_body).encode("utf-8")
            req.data = data
            resp = urllib.request.urlopen(req)
            if resp.status != 200:
                sys.exit(1)
            agent_identifier = resp.headers.get(LAMBDA_AGENT_IDENTIFIER_HEADER_KEY)
            return agent_identifier
        except Exception as e:
            raise Exception(f"Failed to register to ExtensionsAPI: on {self.runtime_api_base_url}/register \
                with agent_unique_name:{agent_unique_name}  \
                and registration_body:{registration_body}\nError: {e}") from e

    def next(self, agent_id):

        try:
            req = urllib.request.Request(f"{self.runtime_api_base_url}/event/next")
            req.method = 'GET'
            req.add_header(LAMBDA_AGENT_IDENTIFIER_HEADER_KEY, agent_id)
            req.add_header("Content-Type", "application/json")
            resp = urllib.request.urlopen(req)
            if resp.status != 200:
                sys.exit(1)
            data = resp.read()
            return data
        except Exception as e:
            raise Exception(f"Failed to get /event/next from ExtensionsAPI: {e}") from e

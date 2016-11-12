import json

import requests


#
# Wunderlist token generation: see README.md
#


class WunderlistConnector:
    api_version = 2
    api_base_url = 'https://a.wunderlist.com/api/v1/'
    client_id = ''
    access_token = ''

    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token

    # --- REQUEST METHODS ---
    def auth(self):
        return

    def get_lists(self):
        request_url = self.api_base_url + 'lists'
        params = {}

        # X-Access-Token: OAUTH-TOKEN X-Client-ID: CLIENT-ID
        headers = {
            'X-Access-Token': self.access_token,
            'X-Client-ID': self.client_id
        }

        response = requests.get(request_url, params=params, headers=headers)

        return json.loads(response.text)

    def get_tasks(self, list_id):
        request_url = self.api_base_url + 'tasks'
        params = {
            'list_id': list_id
        }

        # X-Access-Token: OAUTH-TOKEN X-Client-ID: CLIENT-ID
        headers = {
            'X-Access-Token': self.access_token,
            'X-Client-ID': self.client_id
        }

        response = requests.get(request_url, params=params, headers=headers)

        return json.loads(response.text)
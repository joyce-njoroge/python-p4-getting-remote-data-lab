import requests
import json
import unittest

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content  # Return response as byte string
        except requests.exceptions.RequestException as err:
            print(f'Error occurred during request: {err}')

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            return json.loads(response_body)
        else:
            return None





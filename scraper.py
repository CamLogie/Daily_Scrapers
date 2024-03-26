import requests

class RequestMaker:

    def __init__(self):
        self.base_url = "https://api-web.nhle.com/v1/"

    def make_request(self, endpoint):
        response = requests.get(self.base_url + endpoint)
        return response.json()


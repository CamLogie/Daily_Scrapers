import requests

class RequestMaker:

    base_url = "https://api-web.nhle.com/v1/"

    def make_request(endpoint):
        response = requests.get(RequestMaker.base_url + endpoint)
        return response.json()


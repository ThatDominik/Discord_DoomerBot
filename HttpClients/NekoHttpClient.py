import json
import requests
from FunctionController import is_repeated


class NekoHttpClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_link(self, category):
        response = requests.get(self.api_url + category)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            url = json_data.get("image", None)
            if url:
                if not is_repeated(url):
                    return url
                return self.get_link(category)
            else:
                return "URL not found in API response!"
        else:
            return "Failed to retrieve data from API!"
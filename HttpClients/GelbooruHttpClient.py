import json
import random
import requests
from FunctionController import is_repeated


class GelbooruHttpClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_link(self, category):
        response = requests.get(self.api_url + f"&tags={category}&limit=50&json=1&pid={random.randint(1, 50)}")
        if response.status_code == 200:
            json_data = json.loads(response.text)
            post_list = json_data.get("post", None)
            if len(post_list) == 0:
                return "Api response list is empty!"

            url = post_list[0].get("file_url", None)
            if url:
                if not is_repeated(url):
                    return url
                return self.get_link(category)
            else:
                return "URL not found in API response!"
        else:
            return "Failed to retrieve data from API!"
import json
import random
import requests
import FunctionController
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
                FunctionController.log_event(3, "Api response list is empty!")
                return

            url = post_list[0].get("file_url", None)
            if url:
                if not is_repeated(url):
                    return url
                FunctionController.log_event(1, f"Url repeat for {category} category")
                return self.get_link(category)
            else:
                FunctionController.log_event(3, "URL not found in API response.")
        else:
            FunctionController.log_event(3, f"Failed to retrieve data from API. Response status code {response.status_code}")
        return
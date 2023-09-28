import random
from bs4 import BeautifulSoup
import requests
import FunctionController
from FunctionController import is_repeated


class DictionaryHttpClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_link(self, category):
        response = requests.get(self.api_url + category + f"{random.randint(1, 6)}")
        if response.status_code == 200:
            n_words = []
            html = BeautifulSoup(response.content, 'html.parser')
            word_list = html.findAll('ul', {'class': 'letter__list'})
            for ul in word_list:
                words = ul.findAll('li')
                for word in words:
                    n_words.append(word.text)

            if len(n_words) == 0:
                FunctionController.log_event(3, "No N-words found on url")
                return 'Nenalezeno'
            else:
                word = n_words[random.randint(0, len(n_words)-1)]
                while is_repeated(word):
                    word = n_words[random.randint(0, len(n_words) - 1)]
                return word

        else:
            FunctionController.log_event(3, f"Failed to retrieve N-word data. Response status code {response.status_code}")
            return

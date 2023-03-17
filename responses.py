import constants
import requests
import json

def handle_response(message) -> str:
    message = message.lower()
    if message == "waifu":
        return get_link(constants.WAIFU)
    if message == "neko":
        return get_link(constants.NEKO)
    if message == "bonk":
        return get_link(constants.BONK)
    if message == "hentai":
        return get_link(constants.HENTAI)
    if message == "help":
        return "available commands:\n/doomer waifu\n/doomer bonk\n/doomer hentai\n/doomer neko"
    else:
        return "try /doomer help for all available commands"

def get_link(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        url = json_data.get('url', None)
        if url:
            return url
        else:
            return 'URL not found in API response'
    else:
        return 'Failed to retrieve data from API'
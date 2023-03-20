import constants
import requests
import json

def handle_response(message) -> str:
    message = message.upper()

    if message in constants.commands:
        return get_link(constants.commands[message])
    if message == "HELP":
        return "```available commands:\n/doomer waifu\n" \
               "/doomer bonk\n" \
               "/doomer hentai\n" \
               "/doomer blowjob\n" \
               "/doomer neko\n" \
               "/doomer uwu\n" \
               "/doomer trap\n" \
               "/doomer awoo\n" \
               "/doomer megumin\n/doomer nom```"
    else:
        return "try `/doomer help` for all available commands"

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
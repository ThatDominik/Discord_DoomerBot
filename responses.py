import constants
import requests
import json


def handle_response(message, user) -> str:
    message = message.upper()

    if message in constants.commands:
        command = constants.commands[message]
        # log_social_credits(user, command["karma"])
        return get_link(command["endpoint"])
    if message == "help":
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
            return 'URL not found in API response!'
    else:
        return 'Failed to retrieve data from API!'
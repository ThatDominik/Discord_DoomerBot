import constants
import requests
import json
import os


def handle_response(message, user_id) -> str:
    message = message.upper()
    if message in constants.commands:
        command = constants.commands[message]
        log_karma(user_id, command["karma"])
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


def log_karma(user_id, karma):
    with open(os.getenv("KARMA_LOG"), "w+") as file:
        users_str = file.read()
        if len(users_str) == 0:
            json.dump({user_id: karma}, file)
        else:
            users = json.loads(users_str)
            if user_id in users:
                users[user_id] += karma
            else:
                users[user_id] = karma
        file.close()


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

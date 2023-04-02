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
    # I have to open the file twice, because in r+ mode it appends the json to the existing file when I want to rewrite.
    with open(os.getenv("KARMA_LOG"), "r") as file:
        users_str = file.read()

    with open(os.getenv("KARMA_LOG"), "w") as file:
        if len(users_str) == 0:
            json.dump({user_id: karma}, file)
        else:
            id_string = str(user_id)
            users = json.loads(users_str)
            if id_string in users:
                users[id_string] += karma
            else:
                users[id_string] = karma
            json.dump(users, file)
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

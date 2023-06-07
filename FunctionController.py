import Constants
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
last_images = []
image_buffer = int(os.getenv("IMAGE_REPEAT_BUFFER"))


def save_channel_id(channel_id):
    if channel_id in load_channel_id():
        return "This channel is already subscribed to the daily waifu feed."

    with open(os.getenv("DAILY_CHANNELS"), "a") as file:
        file.write(str(channel_id)+"\n")
        file.close()
    return "You have subscribed to daily waifu picture feed.\nEnjoy!"


def remove_channel_id(channel_id):
    channels = load_channel_id()
    if channel_id not in channels:
        return "This channel is not subscribed to daily feed."

    channels.remove(channel_id)
    with open(os.getenv("DAILY_CHANNELS"), "w") as file:
        for id in channels:
            file.write(str(id)+"\n")
        file.close()
    return "This channel will no longer receive daily spicy pictures."


def load_channel_id():
    with open(os.getenv("DAILY_CHANNELS"), "r") as file:
        id_array = file.readlines()
        for i in range(len(id_array)):
            id_array[i] = int(id_array[i].strip())
        file.close()
    return id_array


def handle_response(message, user_id) -> str:
    message = message.upper()
    if message in Constants.commands:
        command = Constants.commands[message]
        log_karma(user_id, command["karma"])
        return command["client"].get_link(command["category"])
    else:
        return "This category is not implemented yet"


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


def get_user_karma(user_id):
    with open(os.getenv("KARMA_LOG"), "r") as file:
        karma_list = file.read()
        users = json.loads(karma_list)
        if str(user_id) in users:
            return users[str(user_id)]
        return 0


def is_repeated(image_url):
    if image_url in last_images:
        return True

    if len(last_images) >= image_buffer:
        del last_images[0]

    last_images.append(image_url)
    return False

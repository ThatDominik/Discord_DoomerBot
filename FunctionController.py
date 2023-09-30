import datetime
import urllib
import Constants
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
last_images = []
image_buffer = int(os.getenv("IMAGE_REPEAT_BUFFER"))


def save_channel_id(channel_id):
    if channel_id in load_channel_ids():
        return "This channel is already subscribed to the daily waifu feed."

    with open(os.getenv("DAILY_CHANNELS"), "a") as file:
        file.write(str(channel_id)+"\n")
        file.close()
    return "You have subscribed to daily waifu picture feed.\nEnjoy!"


def remove_channel_id(channel_id):
    channels = load_channel_ids()
    if channel_id not in channels:
        return "This channel is not subscribed to daily feed."

    channels.remove(channel_id)
    with open(os.getenv("DAILY_CHANNELS"), "w") as file:
        for id in channels:
            file.write(str(id)+"\n")
        file.close()
    return "This channel will no longer receive daily spicy pictures."


def load_channel_ids():
    try:
        with open(os.getenv("DAILY_CHANNELS"), "r") as file:
            id_array = file.readlines()
            for i in range(len(id_array)):
                id_array[i] = int(id_array[i].strip())
            file.close()
        return id_array
    except FileNotFoundError:
        log_event(1, "File for subscribed channel IDs doesn't exist yet.")
        return []


def handle_response(request, user_id) -> str:
    request = request.upper()
    if request in Constants.commands:
        command = Constants.commands[request]
        try:
            log_karma(user_id, command["karma"])
            return command["client"].get_link(command["category"])
        except Exception as err:
            log_event(3, f"{err=}")
            return "Something went wrong"
    else:
        return "This category is not implemented yet"


def log_karma(user_id, karma):
    users_str = load_karma_data()

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
    karma_list = load_karma_data()
    users = json.loads(karma_list)
    if str(user_id) in users:
        return users[str(user_id)]
    return 0


def load_karma_data():
    try:
        with open(os.getenv("KARMA_LOG"), "r") as file:
            karma_list = file.read()
            return karma_list
    except FileNotFoundError:
        with open (os.getenv("KARMA_LOG"), "w") as file:
            file.close()
        log_event(1, "Creating file for user karma log.")
        return ""


def is_repeated(image_url):
    if image_url in last_images:
        return True

    if len(last_images) >= image_buffer:
        del last_images[0]

    last_images.append(image_url)
    return False


def log_event(severity, message):
    with open(os.getenv("EVENT_LOG"), "a") as file:
        log = ""
        if severity == 1:
            log = "INFO"
        elif severity == 2:
            log = "WARNING"
        elif severity >= 3:
            log = "ERROR"
        file.write(f"{log} {datetime.datetime.now()} -> {message}\n")


def connected():
    try:
        urllib.request.urlopen("http://google.com")
        log_event(1, "Connection check passed.")
        return True
    except:
        log_event(3, "Conection check failed, bot is not connected to the internet.")
        return False
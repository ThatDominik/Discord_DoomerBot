# Discord_DoomerBot
Simple discord bot for sharing lewd anime images from https://waifu.pics/docs, https://www.nekos.fun/apidoc.html and 
https://gelbooru.com/.

# What do you need to start?
- Clone this repo on a server of your choice.
- Create a .env file in Discord_DoomerBot folder where you need to define the following enviromental variables.
```
TOKEN = "YOUR DISCORD BOT TOKEN"
DAILY_CHANNELS = "channel_id.txt"
KARMA_LOG = "karma_log.txt"
EVENT_LOG = "log.txt"
IMAGE_REPEAT_BUFFER = 30
```
The .txt files for channels and karma log will generate automagically. 

IMAGE_REPEAT_BUFFER specifies the number of previous image links the bot checks the new api responses against to prevent 
repeating the same images.
- You will need to install discord.py and python-dotenv packages with the following commands.
``` 
pip install discord.py
pip install python-dotenv
```
- Now you can run main.py to start the bot.
``` 
python3 main.py
``` 
It may take a bit before the bot commands synchronize with all servers the bot is on.




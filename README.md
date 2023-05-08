# Discord_DoomerBot
Simple discord bot for sharing lewd anime images from https://waifu.pics/docs API.

# What do you need to start?
- Clone this repo on a server of your choice.
- Create a .env file in Discord_DoomerBot folder where you need to define the following enviromental variables.
```
TOKEN = "YOUR DISCORD BOT TOKEN"
DAILY_CHANNELS = "channel_id.txt"
KARMA_LOG = "karma_log.txt"
```
The .txt files for channels and karma log should generate automagically, but I didn't test that.
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




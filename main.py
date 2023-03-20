import DoomerBot
import discord
import doomer_bot
import os
from dotenv import load_dotenv, find_dotenv

if __name__ == '__main__':

    #client = doomer_bot.DoomerBot(intents=discord.Intents.default())
    #load_dotenv(find_dotenv())
    #client.run(os.getenv("TOKEN"))
    DoomerBot.run_bot()
import discord
from discord import app_commands
import responses
import os
from dotenv import load_dotenv, find_dotenv


async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


def save_channel_id(channel_id):
    # save it somewhere
    return


def run_bot():
    load_dotenv(find_dotenv())

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    @client.event
    async def on_ready():
        await tree.sync()
        print(f'{client.user}is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if message.content.startswith("/doomer") & message.channel.nsfw:
            user_message = user_message[8:]
            await send_message(message, user_message)

    @tree.command(name="register", description="Registers this channel for daily waifu feed.")  # , guild=discord.Object(id=1086024945928241303) Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
    async def register_command(interaction):
        channel_id = interaction.channel_id
        if interaction.channel.nsfw:
            save_channel_id(interaction.response.send_message(channel_id))
            await interaction.response.send_message("You have subscribed to daily waifu picture feed.\nEnjoy!")
        else:
            await interaction.response.send_message("Only NSFW channels can be subscribed to daily waifu feed.")

    async def send_message_to_channel(channel_id, message):
        try:
            channel = client.get_channel(channel_id)
            await channel.send(message)
        except Exception as e:
            print(e)

    client.run(os.getenv("TOKEN"))

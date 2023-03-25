from typing import Literal
import discord
from discord import app_commands
import responses
import os
from dotenv import load_dotenv, find_dotenv
import doomer_bot


def save_channel_id(channel_id):
    if channel_id in load_channel_id():
        return "This channel is already subscribed to the daily waifu feed."

    with open("channel_id.txt", "a") as file:
        file.write(str(channel_id)+"\n")
        file.close()
    return "You have subscribed to daily waifu picture feed.\nEnjoy!"


def remove_channel_id(channel_id):
    channels = load_channel_id()
    if channel_id not in channels:
        return "This channel is not subscribed to daily waifu feed."

    channels.remove(channel_id)
    with open("channel_id.txt", "w") as file:
        for id in channels:
            file.write(str(id)+"\n")
        file.close()
    return "This channel will no longer receive daily waifu pictures."


def load_channel_id():
    with open("channel_id.txt", "r") as file:
        id_array = file.readlines()
        for i in range(len(id_array)):
            id_array[i] = int(id_array[i].strip())
        file.close()
    return id_array


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = doomer_bot.DoomerBot(intents=intents)
    load_dotenv(find_dotenv())

    @client.event
    async def on_guild_join(guild):
        print("bot joined a nev server")

    @client.tree.command(name="register", description="Registers this channel for daily waifu feed.")
    async def register_command(interaction: discord.Interaction):
        if interaction.channel.nsfw:
            await interaction.response.send_message(save_channel_id(interaction.channel_id))
        else:
            await interaction.response.send_message("Only NSFW channels can register for daily waifu feed.")

    @client.tree.command(name="unsubscribe", description="Unsubscribes this channel from daily waifu feed.")
    async def unsubscribe(interaction: discord.Interaction):
        await interaction.response.send_message(remove_channel_id(interaction.channel_id))

    @client.tree.command(name="pic", description="Receive a spicy picture of the selected category.")
    @app_commands.describe(category="What can I offer you")
    async def picture(
            interaction: discord.Interaction,
            category: Literal['waifu', 'uwu', 'hentai', 'neko', 'trap', 'blowjob', 'awoo', 'megumin', 'bonk', 'nom']
    ):
        if interaction.channel.nsfw:
            response_text = responses.handle_response(category, interaction.user)
            await interaction.response.send_message(f'Here, have a {category} picture!\n{response_text}')
        else:
            await interaction.response.send_message("This command can only be used on NSFW channels.......")

    client.run(os.getenv("TOKEN"))

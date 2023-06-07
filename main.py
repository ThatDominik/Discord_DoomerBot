from typing import Literal
import discord
from discord import app_commands
import os
from dotenv import load_dotenv, find_dotenv
import Constants # Not sure why, but I get import error when I delete this. Like WTF is this language
import DoomerBot
import FunctionController

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    client = DoomerBot.DoomerBot(intents=intents)
    load_dotenv(find_dotenv())

    @client.event
    async def on_guild_join(guild):
        print("bot joined a new server")


    @client.tree.command(name="register", description="Registers this channel for daily feed.")
    async def register_command(interaction: discord.Interaction):
        if interaction.channel.nsfw:
            await interaction.response.send_message(FunctionController.save_channel_id(interaction.channel_id))
        else:
            await interaction.response.send_message("Only NSFW channels can register for daily feed.")


    @client.tree.command(name="unsubscribe", description="Unsubscribes this channel from daily feed.")
    async def unsubscribe(interaction: discord.Interaction):
        await interaction.response.send_message(FunctionController.remove_channel_id(interaction.channel_id))


    @client.tree.command(name="nsfw", description="Receive a spicy picture or gif from the selected category.")
    @app_commands.describe(category="What can I offer you?")
    async def picture(
            interaction: discord.Interaction,
            category: Literal['neko', 'hentai', 'trap', 'blowjob', 'cum', 'lesbian', 'pussy', 'aheago', 'vtuber', 'feet']
    ):
        if interaction.channel.nsfw:
            response_text = FunctionController.handle_response(category, interaction.user.id)
            await interaction.response.send_message(f'Here, have a {category}!\n{response_text}')
        else:
            await interaction.response.send_message("This command can only be used on NSFW channels.")


    @client.tree.command(name="sfw", description="Receive a sfw picture or gif from the selected category.")
    @app_commands.describe(category="What can I offer you?")
    async def picture(
            interaction: discord.Interaction,
            category: Literal['waifu', 'uwu', 'awoo', 'megumin', 'nom', 'bonk']
    ):
        response_text = FunctionController.handle_response(category, interaction.user.id)
        await interaction.response.send_message(f'Here, have a {category}!\n{response_text}')


    @client.tree.command(name="halal_check", description="Check how halal or haram your friend is.")
    @app_commands.describe(victim="Person you want to halal check.")
    async def halal_check(interaction: discord.Interaction, victim: discord.Member):
        karma = FunctionController.get_user_karma(victim.id)
        message = f"{victim.name}'s karma is {karma}.\n"
        if karma >= 0:
            if karma > 50:
                message += f"{victim.name} is a very halal!"
            else:
                message += f"{victim.name} is halal approved!"
        else:
            if karma < -50:
                message += f"By Allah, behave your self {victim.name}! Seriously haram!"
            else:
                message += f"{victim.name} is haram!"

        await interaction.response.send_message(message)


    '''
    @client.tree.command(name="shutdown", description="Shutdown the bot.", guild=discord.Object(id=1086024945928241303))
    async def shutdown(interaction: discord.Interaction):

        await client.close()
    '''

    client.run(os.getenv("TOKEN"))

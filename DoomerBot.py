import datetime
import io
import random
import time
from zoneinfo import ZoneInfo
import aiohttp
from discord.ext import tasks
import discord
from discord import app_commands
import FunctionController


class DoomerBot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        self.daily_feed_send.start()
        self.daily_n_word_send.start()

    async def on_ready(self):
        """
        # For inserting commands to specific servers, currently not working, might use later.
        ids = []
        for guild in self.guilds:
            ids.append(int(guild.id))
        self.tree.copy_global_to(guilds=discord.Object(id=ids)) # for multiple guilds need to change guild to guilds
        """
        # self.tree.clear_commands(guild=None) # for purging commands from servers
        # await self.tree.sync(guild=None)
        await self.tree.sync()
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        FunctionController.log_event(1, "Bot started.")

    @tasks.loop(time=datetime.time(hour=21, minute=00, tzinfo=ZoneInfo("Europe/Prague")))
    async def daily_feed_send(self):
        connected = FunctionController.connected()
        while not connected:
            FunctionController.log_event(2, "Daily feed function sleeping due to bad internet connection.")
            time.sleep(60)
            connected = FunctionController.connected()
        try:
            for channel_id in FunctionController.load_channel_ids():
                channel = self.get_channel(channel_id)
                url = FunctionController.handle_response(
                    random.choice(["hentai", "neko", "trap", "hentai", "neko", "blowjob", "waifu", "vtuber", "feet", "bonk"]),
                    "doomer"
                )
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        img = await resp.read()
                        with io.BytesIO(img) as file:
                            await channel.send(f'Your daily waifu!',file=discord.File(file, url, spoiler=True))
        except Exception as error:
            FunctionController.log_event(3, f"Error during daily feed {error=}\n \t {type(error)=}")

    @daily_feed_send.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

    @tasks.loop(time=datetime.time(hour=9, minute=00, tzinfo=ZoneInfo("Europe/Prague")))
    async def daily_n_word_send(self):
        connected = FunctionController.connected()
        while not connected:
            FunctionController.log_event(2, "Daily feed function sleeping due to bad internet connection.")
            time.sleep(60)
            connected = FunctionController.connected()
        try:
            for channel_id in FunctionController.load_channel_ids():
                channel = self.get_channel(channel_id)
                url = FunctionController.handle_response('nword', "doomer")
                print(url)
                await channel.send(f'The N-word for today is **{url}**.')

        except Exception as error:
            FunctionController.log_event(3, f"Error during daily feed {error=}\n \t {type(error)=}")

    @daily_n_word_send.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

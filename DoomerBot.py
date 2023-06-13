import datetime
import random
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

    @tasks.loop(time=datetime.time(hour=19, minute=00))  # task runs every day at 19:00 utc = 20:00 czech time
    async def daily_feed_send(self):
        for channel_id in FunctionController.load_channel_id():
            channel = self.get_channel(channel_id)
            picture = FunctionController.handle_response(
                random.choice(["hentai", "neko", "trap", "hentai", "neko", "blowjob", "waifu", "vtuber", "feet", "bonk"]),
                "doomer"
            )

            await channel.send(f"Your daily waifu!\n{picture}")

    @daily_feed_send.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

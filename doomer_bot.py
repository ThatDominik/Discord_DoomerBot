from discord.ext import tasks
import discord
from discord import app_commands
import function_controller


class DoomerBot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        self.daily_feed_send.start()

    async def on_ready(self):
        self.tree.copy_global_to(guild=discord.Object(id=1086024945928241303))
        await self.tree.sync(guild=discord.Object(id=1086024945928241303))
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def daily_feed_send(self):
        for channel_id in function_controller.load_channel_id():
            channel = self.get_channel(channel_id)
            await channel.send("background task test")

    @daily_feed_send.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

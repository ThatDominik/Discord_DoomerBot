import datetime
from discord.ext import tasks
import discord
from discord import app_commands
import function_controller
import responses


class DoomerBot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        self.daily_feed_send.start()

    async def on_ready(self):
        """
        # pro nasazování commandů jen na specificke servery, nefunguje, možná se bude hodit idk
        ids = []
        for guild in self.guilds:
            ids.append(int(guild.id))
        guild = discord.Object(id=ids)
        self.tree.copy_global_to(guild=discord.Object(id=ids))
        """
        # self.tree.clear_commands(guild=None) # pro vymazani commandu
        # await self.tree.sync(guild=None)
        await self.tree.sync()
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    @tasks.loop(time=datetime.time(hour=19, minute=00))  # task runs every day at 19:00 utc = 20:00 czech time
    async def daily_feed_send(self):
        for channel_id in function_controller.load_channel_id():
            channel = self.get_channel(channel_id)
            picture = responses.handle_response("hentai", "doomer")
            await channel.send(f"Your daily waifu!\n{picture}")

    @daily_feed_send.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()

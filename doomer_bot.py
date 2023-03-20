from discord.ext import tasks
import discord

class DoomerBot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.daily_feed_send.start()

    """
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    """

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def daily_feed_send(self):
        channel = self.get_channel(1086666091037732876)  # channel ID goes here
        await channel.send("test")


"""
    @daily_feed_send.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in
    

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

#client = DoomerBot(intents=discord.Intents.default())
#client.run(os.getenv("TOKEN"))
"""
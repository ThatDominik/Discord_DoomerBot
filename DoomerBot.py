import discord
import responses

async def send_message(message, userMessage):
    try:
        response = responses.handle_response(userMessage)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = "MTA4NjAyOTg4NzM5NzE4NzYxNw.Gxu53N.KzLaMBiJriAZ43XoGXUbvJfS2UpHctnsRQEueM"

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
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

    client.run(TOKEN)

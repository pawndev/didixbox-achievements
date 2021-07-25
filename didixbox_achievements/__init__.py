import aiohttp
import discord
import io
import os
from urllib.parse import quote

__version__ = '0.1.0'

DEFAULT_IMAGE_HEADER = "ACHIEVEMENT%20UNLOCKED"
DEFAULT_IMAGE_PICTURE = ".png"
discord_token = os.environ.get("DISCORD_TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.split(' ', 1)[1]
    print('Received a message', msg)
    encoded_message = quote(msg)
    image = f'http://www.achievement-maker.com/xbox/{encoded_message}?header={DEFAULT_IMAGE_HEADER}&email=${DEFAULT_IMAGE_PICTURE}'
    async with aiohttp.ClientSession() as session:
        async with session.get(image) as resp:
            if resp.status != 200:
                return await message.channel.send('Uh oh, une erreur est survenue.')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'encoded_message.png'))


def main():
    client.run(discord_token)

if __name__ == '__main__':
    main()


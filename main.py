import discord
import os
from dotenv import load_dotenv
import random

load_dotenv() 

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot_testing_channel_id = 1013948378251542568

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dog_sounds = [
        'bark bark',
        'arf!',
        'woof!',
        'grrrrr',
        'bark',
        'wooooooooooof'
    ]


    if message.content == '!attaboy':
        response = random.choice(dog_sounds)
        print(f'doing a {response} for a user :3')
        await message.channel.send(response)

client.run(os.environ['DISCORD_TOKEN'])

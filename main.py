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

# Shows that bot is intialized
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# A silly starter event that responds to users when they give the bot an attaboy
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
      'wooooooooooof',
      'arf arf',
      'grrrrrrrrrrr',
      'woof woof',
      'woooof',
      'BARK',
      'howl',
      'awooooooo'
    ]

    if message.content == '!attaboy':
        response = random.choice(dog_sounds)
        print(f'doing a {response} for a user :3')
        await message.channel.send(response)

# An event that responds to a user when they post a green square opportunity
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # If message contains 'green square opportunity' & 'github link' then respond with something positive
    if ('green' in message.content) and ('square' in message.content) and ('opportunity' in message.content) and ('/github.com/' in message.content):
      print('someone posted a green square opportunity!')
      emoji = '🦾'

      exclaimations = [
        'Holy smoke!',
        'Holy smokes!',
        'Wow!',
        'Woweeee!',
        'Way to go!',
        'Whoooooo!',
        'Hooray!',
        'Hooya!',
        'Huzzah!',
        'Yes!',
        '!!!!!!!!!!!!!',
        'Well lookie here!',
        'Awww!',
        'Brilliant!',
        'Excellent!',
        'Awesome!'
      ]
      await message.add_reaction(emoji)
      await message.reply(random.choice(exclaimations) + f" Thanks for sharing this green square opportunity, @{message.author.name}!")

# Runs app using Discord token
client.run(os.environ['DISCORD_TOKEN'])

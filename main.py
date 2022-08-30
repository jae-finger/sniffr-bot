import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv() 

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot_testing_channel_id = 1013948378251542568

# This example requires the 'members' and 'message_content' privileged intents to function.

bot = commands.Bot(command_prefix='?', description=description, intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# @bot.event
# async def on_message(message):
#    if message.content == 'hello bot':
#       await message.reply("Yo!")
     

@bot.command(name='attaboy')
async def _bot(message):
  """sniffr_bot help command"""
  if message.author == bot.user:
        return

  else:
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
      'awooooooo',
      'bow-wow',
      'woof-woof',
      ''
    ]
    response = random.choice(dog_sounds)
    print(f'doing a {response} for a user :3')
    await message.reply(response)

@bot.command(name='help')
async def _bot(ctx):
    """sniffr_bot help command"""
    await ctx.reply(f"""Hello, {ctx.author.name}! sniffr_bot and its help system are currently under construction. Current working commands are:
    *?attaboy*       Call sniffr_bot over for an 'atta boy!'""")

      
# Runs app using Discord token
bot.run(os.environ['DISCORD_TOKEN'])

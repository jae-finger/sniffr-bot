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

@bot.command()
async def help(ctx):
  """sniffr_bot help command"""
  print(f"Helping out {ctx.author.name}")
  await ctx.reply(f"""Hello, {ctx.author.name}! sniffr_bot and its help system are currently under construction. Current working commands are:
  *?attaboy*       Call sniffr_bot over for an 'atta boy!'""")

@bot.command()
async def attaboy(ctx):
  """sniffr_bot help command"""
  if ctx.author == bot.user:
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
    await ctx.reply(response)
  
@bot.listen('on_message')
async def green_square_bot(message):
    if message.author == bot.user:
        return
    # If message contains 'green square opportunity' & 'github link' then respond with something positive
    if ('green' in message.content) and ('square' in message.content) and ('github.com/the-best-team-seven/sniffr' in message.content):
      print(f'{message.author.name} posted a green square opportunity!')
      emoji = '🦾'

      exclamations = [
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
        'Awesome!',
        'Nani!?'
      ]
      
      await message.add_reaction(emoji)
      await message.reply(random.choice(exclamations) + f" Thanks for sharing this green square opportunity, @{message.author.name}!")
      
# Runs app using Discord token
bot.run(os.environ['DISCORD_TOKEN'])

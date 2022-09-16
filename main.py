import discord
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
import random
import spacy
from spacy.matcher import Matcher
import re
import datetime
import requests
import asyncio

# Load env variables
load_dotenv() 

# Load spacy stuff
nlp = spacy.load("en_core_web_md")
matcher = Matcher(nlp.vocab)

# Define discord bot data
description = '''A discord bot serving sniffr developers and users!'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot_testing_channel_id = 1013948378251542568
sniffr_main_channel_id = 1013694573651959808

bot = commands.Bot(command_prefix='?', description=description, intents=intents, allowed_mentions = discord.AllowedMentions(everyone = True))
bot.remove_command("help")

## Keep track of both backend and frontend pull requests
# If a new pull request has a higher id than these, then it's new
backend_pull_id = 0
frontend_pull_id = 0

## Text variables
mech_arm_emoji = '🦾'

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
  'Nani!?',
  '?!',
  '👀',
  '🤯'
]

# Login event
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id}) at {datetime.datetime.now()} ')
    print('------')

    # if not meeting_time_message.is_running():
    #     meeting_time_message.start() #If the task is not already running, start it.
    #     print("meeting_time_message task started")

#################################################################################
## Bot commands

# Help command
@bot.command(name='help')
async def Help_Command(ctx):
  """sniffr_bot help command"""
  print(f"Helping out {ctx.author.name}")
  await ctx.reply(f"""Hello, {ctx.author.name}! sniffr_bot and its help system are currently under construction. Current working commands are:
  *?attaboy*        Call sniffr_bot over for an 'atta boy!'
  *?server_urls*   Returns the web addresses for front and back end production servers
  *?dogpic*          Get a random dog picture
  """)

# Attaboy command
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
      'woof-woof'
    ]
    response = random.choice(dog_sounds)
    print(f'doing a {response} for a user :3')
    await ctx.reply(response)

# Server URLs command
@bot.command()
async def server_urls(ctx):
  """sniffr_bot help command"""
  if ctx.author == bot.user:
        return
  response = """**front end:** https://team-sniffr.netlify.app/  
**back end:** http://sniffr-be.herokuapp.com/
  """
  
  print(f'{ctx.author} asked for the fe/be servers')
  await ctx.reply(response)
  
# Dog pic command
@bot.command(name='dogpic', aliases=['dogimg'])
async def DogPic(ctx):
  '''Get a dog picture from a api randomly'''
  if ctx.author == bot.user:
      return
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  image_link = response.json()["message"]
  print(f"Sending {ctx.author} an image ({image_link})")
  await ctx.send(image_link)

# Meeting Messages (meetingmsg eta5meetingmsg)
@bot.command(name='meetingmsg')
async def schedule_meeting_message(ctx, meetinglink = ''):
  if ctx.author == bot.user:
      return

  today = datetime.date.today()
  # monday = 0, sunday = 6
  if today.weekday() in [2, 5]:
    channel = bot.get_channel(sniffr_main_channel_id)
    print("Reminding people that there is a meeting now!")
    await channel.send(f"""🐶sniffr team... ASSEMBLE! It's meeting time🐩 (@everyone)🐕  
    Zoom link: {meetinglink}""")

@bot.command(name='eta5meetingmsg')
async def eta5_message_message(ctx):
  if ctx.author == bot.user:
      return
  today = datetime.date.today()
  # monday = 0, sunday = 6
  if today.weekday() in [2, 5]:
    channel = bot.get_channel(sniffr_main_channel_id)
    print("Reminding people that there is a meeting soon~~")
    await channel.send("""Who's ready for some sniffr action? There's a meeting coming in 5 minutes, @everyone!""")

# Fetch env s
@bot.command(name='fetch_env')
async def download_envs(ctx, repo = ''):
  if ctx.author == bot.user:
      ...

  # fix repo name
  repo = repo.lower()

  # if requesting fe
  if (repo == 'fe') or (repo == 'frontend') or (repo == 'front end'):
    await ctx.author.send('''
    `FE`
    ''')
  
  # elif reqesting be
  elif (repo == 'be') or (repo == 'backend') or (repo == 'backend'):
    await ctx.author.send('BE')

  # return nothing if else
  else:
    ...

## Bot Events
@bot.listen('on_message')
async def green_square_bot(message):
    if message.author == bot.user:
        return

    message_content = message.content.lower()

    ## If message contains a front end or back end url then track and respond
    # Does the message contain a front end or backend url?
    # Front end
    if 'github.com/the-best-team-seven/' in message_content:
      # Extract pull id
      global frontend_pull_id, mech_arm_emoji, exclamations, backend_pull_id
      doc = nlp(message_content)

      for token in doc:
        # if github fe in pull request found
        if '/sniffr-fe/pull/' in token.text:
          pattern = r"[0-9]+"
          matches = re.findall(pattern, token.text)
          pull_id = int(matches[0])

          # if this pull is new, then respond
          if pull_id > backend_pull_id:
            backend_pull_id = pull_id
            print(f'{message.author.name} posted a green square opportunity!')

            await message.add_reaction(mech_arm_emoji)
            await message.reply(random.choice(exclamations) + f" Thanks for sharing this green square opportunity, {message.author.name}!")

        # if github be in pull request found
        elif '/sniffr-be/pull/' in token.text:
          pattern = r"[0-9]+"
          matches = re.findall(pattern, token.text)
          pull_id = int(matches[0])

          # if this pull is new, then respond
          if pull_id > backend_pull_id:
            backend_pull_id = pull_id
            print(f'{message.author.name} posted a green square opportunity!')

            await message.add_reaction(mech_arm_emoji)
            await message.reply(random.choice(exclamations) + f" Thanks for sharing this green square opportunity, {message.author.name}!")
    else:
      ...

if __name__ == '__main__':
  # Runs app using Discord token
  bot.run(os.environ['DISCORD_TOKEN'])

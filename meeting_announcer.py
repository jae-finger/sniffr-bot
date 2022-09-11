import datetime

# Create tuesday eta5 meeting time and actual meeting time (5pm central)
tuesday_meeting_time_eta5 = datetime.time(hour=17, minute=55, second=0)
tuesday_meeting_time = datetime.time(hour=18, minute=0, second=0)

# Create tuesday eta 5 meeting task
@tasks.loop(time=tuesday_meeting_time_eta5)
async def eta5_minutes():
    channel = client.get_channel(bot_testing_channel_id)
    await channel.send("ETA 5 minutes until a sniffr meeting, yo!")
    print("Reminding people that there is a meeting soon")


@client.event
async def on_ready():
    if not eta5_minutes.is_running():
        eta5_minutes.start() #If the task is not already running, start it.
        print("ETA 5 mins till meeting task started")
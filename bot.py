# bot.py

import os
import discord
import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')

client = discord.Client()

MEMBER = client.get_user(238093622568812544)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    
@client.event
async def on_voice_state_update(MEMBER, before: discord.VoiceState, after: discord.VoiceState) -> None:
    check_time = datetime.now(tz.utc)
    dotw = datetime.now().weekday()
    cutoff = check_time.replace(hour=22, minute=0, second=0, microsecond=0)
    
    print(f'Detected User at {check_time}.')
    
    if dotw < 5 and check_time < cutoff:
        if after.channel is None:
            return
        else:
            print(f'Attempting to Disconnect User.')
            await MEMBER.edit(voice_channel=None)
    else:
        return
    
client.run(TOKEN)
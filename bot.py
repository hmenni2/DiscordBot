# bot.py

import os
import discord
from datetime import datetime, time
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
    check_time = datetime.utcnow().time
    dotw = datetime.now().weekday()
    
    if dotw < 5 & checktime <= time(21,59):
        if after.channel is None:
            return
        else:
            await MEMBER.edit(voice_channel=None)
    else:
        return
    
client.run(TOKEN)
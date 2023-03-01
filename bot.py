# bot.py

import os
import discord
from datetime import datetime, time
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MEMBER = client.get_user(238093622568812544)

client = discord.Client()

@client.event
async def on_ready():
    printf(f'{client.user} has connected to {GUILD}.')
    
@client.listen()
async def on_voice_state_update(MEMBER, before: discord.VoiceState, after: discord.VoiceState) -> None:
    check_time = datetime.uutcnow().time
    
    if checktime <= time(21,59):
        if after.channel is None:
            return
        else:
            await MEMBER.edit(voice_channel=None)
    else:
        return
    
client.run(TOKEN)
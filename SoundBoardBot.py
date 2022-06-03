# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:38:26 2022

@author: chanc
"""

# bot.py


from multiprocessing.connection import wait
import os
from time import sleep

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from dotenv import load_dotenv


#load_dotenv()
load_dotenv('Auth.env')
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = "!")
"""
@client.event
async def on_ready():
   for guild in client.guilds:
       if guild.name == SERVER:
           break
       
   channel = discord.utils.get(guild.voice_channels, name='General',bitrate=64000)
   voice = discord.VoiceProtocol(client,channel)
   timeout = float(100000)
   reconnect = False

   voice.connect(timeout,reconnect)
"""
@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("you are not connected to a channel")
        await ctx.message.delete()  

@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I LEFT")
        await ctx.message.delete()  
    else:
        await ctx.send("I am not in a channel")
        await ctx.message.delete()  

@client.command(pass_context = True)
async def sounds(ctx):
    await ctx.send(os.listdir("./Sounds"))
    



@client.command(pass_context=True)
async def Play(ctx,soundname):
    if(ctx.voice_client==False):
        await join(ctx)
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('./Sounds/'+soundname+'.mp3')
        player =  voice.play(source)
        while voice.is_playing():
            sleep(.1)
        await voice.disconnect()

    await ctx.message.delete()   
   
@client.command(pass_context=True)
async def play(ctx,soundname):
    if(ctx.voice_client==False):
        await join(ctx)
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('./Sounds/'+soundname+'.mp3')
        player =  voice.play(source)
        while voice.is_playing():
            sleep(.1)
        await voice.disconnect()

    await ctx.message.delete()    


client.run(TOKEN)

#TOKEN = os.getenv("OTgyMzE2Njk3MDEwNzI5MDAw.GV48WX.CoPnswIMdlbhZIsNJgqnI5SkdZiVcdXiQq7Y6o")

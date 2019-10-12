import discord
import json
import os
import logging
import datetime
from discord.ext import commands

#########################################
#                                       #
#             Meta Stuff                #
#                                       #
#########################################

# Basic logging @TODO: expand on logging
log = logging.getLogger('discord')
log.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='marvin.log',encoding='utf-8', mode='w')
log.addHandler(handler)

# Load in keys.json and config.json
with open('keys.json', 'r') as rk, open('config.json', 'r') as rc:
    keys, config = json.load(rk), json.load(rc)

client = commands.Bot(command_prefix=config['prefix'], owner_id=config['ownerid'], description="Hello, I am Marvin. I look forward to your company. \n Please visit hellomarvin.org for any furthur help")



@client.event
async def on_ready():
    print(f'---------------------\n@READY: {client.user.name}: {datetime.datetime.now()}\n---------------------')

    # Set game Marvin is playing
    await client.change_presence(activity=discord.Game('m.help'))

    client.remove_command('help')

    # Initial load of Cog files
    for filename in os.listdir('./cogs'):
        if filename.endswith('py'):
            try:
                client.load_extension(f'cogs.{filename[:-3]}')
            except Exception as e:
                print(f'{filename} cog can not be loaded')
                raise e

#########################################
#                                       #
#         Cog Related Commands          #
#                                       #
#########################################

# Load Cogs
@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} cog has loaded')
    except Exception as e:
        print(f'{extension} cog could not be loaded')
        raise e

# Unload a Cog
@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} cog unloaded')
    except Exception as e:
        print(f'{extension} cog could not be unloaded')
        raise e

# Reload a cog (unloading and reloading)
@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} cog reloaded')
    except Exception as e:
        print(f'{extension} cog could not be reloaded')
        raise e


# Run bot with api key
client.run(keys['discordapi'])

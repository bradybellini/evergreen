import discord
import json
import os
import logging
import datetime
from discord.ext import commands


# class Marvin(commands.Bot):

#     async def on_ready(self):
#         print('Logged on as', self.user)
#         await Marvin.change_presence(self, activity=discord.Game
#                                      ('hellomarvin.org'))
    
#     # @Marvin.command(hidden=True, aliases=['kill', 'stop'])
#     # async def kill_bot(self, ctx):
#     #     await Marvin.logout()


# command_prefix = 'm.'
# description = 'Hello, I am Marvin'
# owner_id = 101563945462026240
# bot = Marvin(command_prefix=command_prefix, description=description,
#              owner_id=owner_id)
# bot.run(discord_apikey)


log = logging.getLogger('discord')
log.setLevel(logging.INFO)
handler = logging.FileHandler(filename='marvin.log',encoding='utf-8', mode='w')
log.addHandler(handler)

# Load in keys.json and config.json
with open('keys.json', 'r') as rk, open('config.json', 'r') as rc:
    keys, config = json.load(rk), json.load(rc)

client = commands.Bot(command_prefix=config['prefix'], owner_id=config['ownerid'], description="Hello, I am Marvin. I look forward to your company. \n Please visit hellomarvin.org for any furthur help")


@client.event
async def on_ready():
    print(f'---------------------\n@READY: {client.user.name}: {datetime.datetime.now()}\n---------------------')
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

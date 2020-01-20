import discord
import json
import os
import logging
import datetime
import asyncpg
import asyncio
from apikeys import pgpswd
from apikeys import discordapi
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
# with open('config.json', 'r') as rc:
#     config = json.load(rc)

client = commands.Bot(command_prefix='e.', owner_id=101563945462026240, description="change this")

#mess around with pooling size and when innactive connections should be terminiated.
#Look at the asyncpg docs with connection pooling. This needs to be optimized because I think it will have alot to do with the repsonse speed.
async def create_db_pool():
    credentials = 'postgresql://evergreen:' + pgpswd + '@psql-sfo2-01-do-user-4855641-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require'
    client.pg_conn = await asyncpg.create_pool(dsn=credentials, min_size=2, max_size=22)


@client.event
async def on_ready():
    print(f'---------------------\n@READY: {client.user.name}: {datetime.datetime.now()}\n---------------------')

    # Set game Marvin is playing
    await client.change_presence(activity=discord.Game('e.help'))

    # client.remove_command('help')

    # Initial load of Cog files
    for filename in os.listdir('./cogs'):
        if filename.endswith('py') and not filename.startswith('_'):
            try:
                client.load_extension(f'cogs.{filename[:-3]}')
            except Exception as e:
                print(f'#### {filename} cog can not be loaded ####')
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


client.loop.run_until_complete(create_db_pool())

# Run bot with api key
client.run(discordapi)

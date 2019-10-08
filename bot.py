import discord
from discord.ext import commands
from apikeys import discord_apikey


class Marvin(commands.Bot):

    async def on_ready(self):
        print('Logged on as', self.user)
        await Marvin.change_presence(self, activity=discord.Game
                                     ('hellomarvin.org'))
    
    # @Marvin.command(hidden=True, aliases=['kill', 'stop'])
    # async def kill_bot(self, ctx):
    #     await Marvin.logout()


command_prefix = 'm.'
description = 'Hello, I am Marvin'
owner_id = 101563945462026240
bot = Marvin(command_prefix=command_prefix, description=description,
             owner_id=owner_id)
bot.run(discord_apikey)

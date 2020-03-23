import discord
from discord.ext import commands

class Error(commands.Cog, name='Errors'):

    def __init__(self, client):
        self.client = client

    # async def on_command_error(self, ctx, error):
    #     await ctx.send(error)

def setup(client):
    client.add_cog(Error(client))
    print('@COG: Error Cog loaded \n---------------------')
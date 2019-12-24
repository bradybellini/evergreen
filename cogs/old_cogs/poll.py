import discord
from discord.ext import commands

class Poll(commands.Cog, name="Poll Cog"):
    pass

def setup(client):
    client.add_cog(Poll(client))
    print('@COG: Poll Cog loaded \n---------------------')
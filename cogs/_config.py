import discord
import json
from discord.ext import commands


class Config(commands.Cog):
    pass

def setup(client):
    client.add_cog(Config())
    print('@COG: Config Cog loaded \n---------------------')

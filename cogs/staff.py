import discord
from datetime import datetime
from discord.ext import commands

class Staff(commands.Cog, name='Staff commands'):
    """Staff related commands"""
    def __init__(self, client):
        self.client = client




def setup(client):
    client.add_cog(Staff(client))
    print('@COG: Minecraft Cog loaded \n---------------------')
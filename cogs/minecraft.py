import discord
from discord.ext import commands

class Minecraft(commands.Cog, name='Minecraft commands'):
    """Minecraft related commands"""
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Minecraft(client))
    print('@COG: Minecraft Cog loaded \n---------------------')

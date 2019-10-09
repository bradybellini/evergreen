import discord
import json
from discord.ext import commands


class Config(commands.Cog):

    def __init__(self):
        with open('keys.json', 'r') as rk, open('config.json', 'r') as rc:
            keys, config = json.load(rk), json.load(rc)
        self.apikey = keys['discordapi']
        self.test = config['test']


def setup(client):
    client.add_cog(Config())
    print('Config Cog loaded \n---------------------')

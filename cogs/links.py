import discord
import sqlite3
import re
from datetime import datetime
from discord import Message, TextChannel, Member, PartialEmoji
from discord.ext import commands

class Links(commands.Cog, name="Keep track of urls posted in your server"):

    def __init__(self, client):
        self.client = client







def setup(client):
    client.add_cog(Links(client))
    print('@COG: Link Cog loaded \n---------------------')
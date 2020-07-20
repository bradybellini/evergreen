import discord
from discord import TextChannel, PartialEmoji
from discord.ext import commands


class Polls(commands.Cog, name="polls"):

    def __init__(self, client):
        self.client = client
        self.reactions = ['🇦', '🇧', '🇨', '🇩', '🇪', '🇫']

    @commands.group(invoke_without_command=True, aliases=['polls', 'strawpoll'])
    async def poll(self, ctx):
        pass

    @commands.has_permissions(administrator=True)
    @poll.command()
    async def new(self, ctx, *, content):
        ": Create a new poll"
        pass


def setup(client):
    client.add_cog(Polls(client))
    print('@COG: Polls Cog loaded \n---------------------')

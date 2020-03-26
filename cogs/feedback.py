import discord
from datetime import datetime
from discord.ext import commands


class Feedback(commands.Cog, name="Feedback"):
    """Submit feedback"""

    def __init__(self, client):
        self.client = client

    
    @commands.group(invoke_without_command=True, alias=['suggest', 'fb', 'idea'])
    @commands.cooldown(1, 1800, type=commands.BucketType.user)
    async def feedback(self, ctx):
        pass

    @feedback.command()
    async def new(self, ctx, *, content=None):
        await ctx.send("test")

def setup(client):
    client.add_cog(Feedback(client))
    print('@COG: Feedback Cog loaded \n---------------------')

import discord
import datetime
from discord.ext import commands


class Meta(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True, aliases=['kill', 'stop'])
    @commands.is_owner()
    async def kill_bot(self, ctx):
        await ctx.send('Shutting down...')
        await ctx.send('Goodbye')
        await self.client.logout()

    @commands.command()
    async def ping(self, ctx, ping=None):
        if ping == None:
            await ctx.send(f'Pong! Latency to Marvin: `{round(self.client.latency * 1000)}ms`')
        else:
            await ctx.send('no ping for you')

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(colour=0xff7b,)
        embed.timestamp =  datetime.datetime.utcnow()
        embed.set_author(name="Support the Development of Marvin!", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name="Get Marvin Prime!", value="Get premium features like cool and cool!")
        embed.add_field(name="Get free digital ocean money!", value="use this link and get free digital ocean money!")
        embed.add_field(name="Another way to support", value="share marvin invite link!")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Meta(client))
    print('@COG: Meta Cog loaded \n---------------------')

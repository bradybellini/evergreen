import discord
import datetime
import argparse
from discord.ext import commands


class Meta(commands.Cog, name="meta"):

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
        """: Check latency to Marvin"""
        if not ping:
            await ctx.send(f'Pong! Latency to Marvin: `{round(self.client.latency * 1000)}ms`')
        else:
            await ctx.send('no ping for you')

    @commands.command(hidden=True)
    async def support(self, ctx):
        """: Support the development of Evergreen"""
        embed = discord.Embed(colour=0xff7b,)
        embed.timestamp =  datetime.datetime.utcnow()
        embed.set_author(name="Support the Development of Marvin!", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name="Get Marvin Prime!", value="Get premium features like cool and cool!")
        embed.add_field(name="Get free digital ocean money!", value="use this link and get free digital ocean money!")
        embed.add_field(name="Another way to support", value="share marvin invite link!")
        await ctx.send(embed=embed)

    @commands.command()
    async def guildowner(self, ctx):
        guild_owner = ctx.guild.owner
        # owner_member = 
        await ctx.send(guild_owner)


# Look into testing out argparse more for complex commands
    # @commands.command()
    # async def argtest(self, ctx, test=None):
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument("z")
    #     args = parser.parse_args(test)
    #     await ctx.send(args.z)

def setup(client):
    client.add_cog(Meta(client))
    print('@COG: Meta Cog loaded \n---------------------')

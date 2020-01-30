import discord
import datetime
import aiosqlite
from discord.ext import commands


class Meta(commands.Cog, name="meta"):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True, aliases=['kill', 'stop'])
    @commands.is_owner()
    async def kill_bot(self, ctx):
        ": Shuts down the bot on the server"
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

    @commands.command()
    async def addguild(self, ctx):
        db = await aiosqlite.connect('marvin.db')
        cursor = await db.cursor()
        sql = ('INSERT INTO guilds(guild_id, guild_owner) VALUES(?,?)')
        val = (str(ctx.guild.id), str(ctx.guild.owner.id))
        await cursor.execute(sql,val)
        await db.commit()
        await cursor.close()
        await db.close()


    @commands.command(hidden=True)
    async def support(self, ctx):
        pass

    @commands.command()
    async def guildowner(self, ctx):
        ": displays the current owner of the current guild"
        guild_owner = ctx.guild.owner
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

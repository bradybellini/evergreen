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
    @commands.cooldown(1, 10, type=commands.BucketType.user)
    async def ping(self, ctx, ping=None):
        ": Check latency to Marvin"
        if not ping:
            await ctx.send(f'Pong! Latency to Marvin: `{round(self.client.latency * 1000)}ms`')
        else:
            await ctx.send('no ping for you')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def addguild(self, ctx):
        ": Adds guild to db !Should not need to use!"
        db = await aiosqlite.connect('marvin.db')
        cursor = await db.cursor()
        sql = ('INSERT INTO guilds(guild_id, guild_owner) VALUES(?,?)')
        val = (str(ctx.guild.id), str(ctx.guild.owner.id))
        await cursor.execute(sql, val)
        await db.commit()
        await cursor.close()
        await db.close()

    @commands.command(hidden=True)
    async def support(self, ctx):
        pass

    @commands.command(hidden=True)
    async def guildowner(self, ctx):
        ": displays the current owner of the current guild"
        guild_owner = ctx.guild.owner
        await ctx.send(guild_owner)

    @ping.error
    async def ping_error(self, ctx, error):
        embed = discord.Embed(title=f" Try again in {int(error.retry_after)} seconds.", colour=0xd95454)
        embed.set_author(name=f"You are on a cooldown for this command!")
        # time_left = int(error.retry_after//60)
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Meta(client))
    print('@COG: Meta Cog loaded \n---------------------')

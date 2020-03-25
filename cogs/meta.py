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

    @commands.command()
    async def welcomemessage(self, ctx):
        join_message = """:small_orange_diamond: Welcome to InfinityCraft 2.∞! If you need help make sure to check out the #help channel or run the command `m.help` to get Marvin(me) to give you command help within the server. 
:small_orange_diamond: I may take some time to respond to your command so please be patient. I am a cactus after all. 
:small_blue_diamond: Make sure to run the command `/discord link` in Minecraft to link your Minecraft and Discord account and follow the directions given. You should get the Voyager rank as well as some other perks. 
:small_blue_diamond: To submit a report or ticket, check out the #ticket channel. 
:small_blue_diamond: Last of all, make sure to follow all the rules posted in the #rules channel. 
:small_blue_diamond: If you have any further questions, feel free to ask a staff member or other members of the community.

Server IP: `mc.gamersgrove.net`
Website: https://infinity.gamersgrove.net/
Discord Invite Link: https://discordapp.com/invite/v67aGnq or https://discord.gamersgrove.net"""
        await ctx.send(join_message)

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

import discord
import aiosqlite
import time
import random
import string
from datetime import datetime
from discord.ext import commands

class Tickets(commands.Cog, name="tickets"):
    """Ticket commands"""
    def __init__(self, client):
        self.client = client
        # self.loop = asyncio.get_event_loop()

    @commands.group(invoke_without_command=True)
    async def ticket(self, ctx, content=None):
        pass
        # db = await aiosqlite.connect('evergreen.db')

    @ticket.command()
    async def setchannel(self, ctx):
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        sql = ('UPDATE guilds SET ticket_channel = ? WHERE guild_id = ?')
        val = ( str(ctx.channel.id), str(ctx.guild.id))
        await cursor.execute(sql,val)
        await db.commit()
        await cursor.close()
        await db.close()

# UPDATE guilds SET ticket_channel = ? WHERE guild_id = ?
# INSERT INTO guilds(ticket_channel) WHERE guild_id = ?, VALUES(?)
    @commands.has_permissions(administrator=True)
    @ticket.command()
    async def panel(self, ctx, name=None):
        await ctx.send('new panel')


# edit embed to change color based on ticket status maybe
# add reactions to control ticket status and reponse
# add in the message ID and find a way to get the message Id and send the message and update it with ticket id, just need to find the order
# edit embed message after it was sent to change the color to match the status of the ticket.
# might need to change ticket context to not have guild id be checked if we want tickets sent via dms
    @ticket.command()
    async def new(self, ctx, *, content):
        db = await aiosqlite.connect('main.db')
        cursor = await db.cursor()
        try:
            ticket_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
            created = int(datetime.utcnow().timestamp())
            sql = ('INSERT INTO tickets(ticket_id, guild_id, author, content, created) VALUES(?,?,?,?,?)')
            val = (ticket_id, str(ctx.guild.id), str(ctx.message.author.id), str(content), created)
            await cursor.execute(sql,val)
            await db.commit()
        except:
            ticket_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
            created = int(datetime.utcnow().timestamp())
            sql = ('INSERT INTO tickets(ticket_id, guild_id, author, content, created) VALUES(?,?,?,?,?)')
            val = (ticket_id, str(ctx.guild.id), str(ctx.message.author.id), str(content), created)
            await cursor.execute(sql,val)
            await db.commit()

        embed = discord.Embed(title=f"New Ticket - {ticket_id}", colour=0x90ff)
        embed.add_field(name="Ticket author", value=f"{ctx.message.author}")
        embed.add_field(name="Content", value=f"{content}", inline=False)
        embed.add_field(name="Status", value="Open", inline=False)
        embed.add_field(name="Response", value=f"none", inline=False)
        embed.add_field(name="Response by", value=f"none", inline=False)
        embed.add_field(name="Response Date", value=f"none", inline=False)
        embed.add_field(name="Created", value=f"{datetime.fromtimestamp(created)} UTC", inline=False)
        sql = ('SELECT ticket_channel FROM guilds WHERE guild_id = ?')
        val = (str(ctx.guild.id),)
        await cursor.execute(sql,val)
        channel_id = await cursor.fetchone()
        await cursor.close()
        await db.close()
        channel = self.client.get_channel(int(channel_id[0]))
        await channel.send(embed=embed)
        await ctx.message.author.send(embed=embed)


    @new.error
    async def new_ticket_error(self, ctx, error):
        embed = discord.Embed(title="Try: m.ticket new [content]", colour=0xd95454)
        embed.set_author(name=f"{error}", url="https://discordapp.com")
        embed_forb = discord.Embed(title="Try: m.kick [user] <reason>", colour=0xd95454)
        embed_forb.set_author(name="Missing Permissions", url="https://discordapp.com")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Tickets(client))
    print('@COG: Ticket Cog loaded \n---------------------')

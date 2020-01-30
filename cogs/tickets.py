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

    @commands.group(invoke_without_command=True, aliases=['tickets', 't'])
    async def ticket(self, ctx):
        pass

    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    @ticket.command()
    async def setchannel(self, ctx):
        "Sets the channel new tickets are sent to"
        db = await aiosqlite.connect('marvin.db')
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
    @commands.guild_only()
    @ticket.command()
    async def panel(self, ctx, name=None):
        "Create a new ticket panel"
        await ctx.send('new panel')


# this is not going to happen at the moment, its better to send a new message because they wont get a notification otherwise : edit embed to change color based on ticket status maybe
# not going to happen as I feel like it will make people not want to repsond to a ticket : add reactions to control ticket status and reponse
# fixed only for this fork as its only used in one server : might need to change ticket context to not have guild id be checked if we want tickets sent via dms
    @ticket.command()
    async def new(self, ctx, *, content):
        "Create a new ticket"
        db = await aiosqlite.connect('marvin.db')
        cursor = await db.cursor()
        try:
            ticket_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
            created = int(datetime.utcnow().timestamp())
            sql = ('INSERT INTO tickets(ticket_id, author, content, created) VALUES(?,?,?,?)')
            val = (ticket_id, str(ctx.message.author.id), str(content), created)
            await cursor.execute(sql,val)
            await db.commit()
        except:
            ticket_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
            created = int(datetime.utcnow().timestamp())
            sql = ('INSERT INTO tickets(ticket_id, author, content, created) VALUES(?,?,?,?)')
            val = (ticket_id, str(ctx.message.author.id), str(content), created)
            await cursor.execute(sql,val)
            await db.commit()

        embed = discord.Embed(title=f"New Ticket - {ticket_id}", colour=0xfd70)
        embed.add_field(name="Ticket author", value=f"{ctx.message.author}")
        embed.add_field(name="Content", value=f"{content}", inline=False)
        embed.add_field(name="Status", value="Open", inline=False)
        embed.add_field(name="Response", value=f"none", inline=False)
        embed.add_field(name="Response by", value=f"none", inline=False)
        embed.add_field(name="Response Date", value=f"none", inline=False)
        embed.add_field(name="Created", value=f"{datetime.fromtimestamp(created)} UTC", inline=False)
        sql = ('SELECT ticket_channel FROM guilds WHERE guild_id = ?')
        val = (str(610914837039677471),)
        await cursor.execute(sql,val)
        channel_id = await cursor.fetchone()
        await cursor.close()
        await db.close()
        channel = self.client.get_channel(int(channel_id[0]))
        await channel.send(embed=embed)
        await ctx.message.author.send(embed=embed)

# Response is not working. No errors are being thrown, but nothing is being inputed into the database, queuery seems to be right but I cant tell if that is the problem or not
# aliases=['r', 'reply']
    # @commands.has_permissions(administrator=True)
    @ticket.command()
    async def respond(self, ctx, ticket_id, *,content):
        "Reply/Repsond to a ticket"
        db = await aiosqlite.connect('marvin.db')
        response_date = int(datetime.utcnow().timestamp())
        cursor = await db.cursor()
        sql = ("UPDATE tickets SET response = ? , responder = ? , response_date = ? WHERE ticket_id = ?")
        val = (str(content), str(ctx.message.author.id), response_date, str(ticket_id))
        await cursor.execute(sql,val)
        # this god damn module wasnt working because I forgot to commit the fucking data. I spent hours trying to fix this.
        # will clean up later
        await db.commit()
        # except Exception as e:
        #     await ctx.send(e)
        # sql = ('SELECT author FROM tickets WHERE ticket_id = ?')
        # val = (ticket_id,)
        # await cursor.execute(sql,val)
        # user_id = await cursor.fetchone()
        # user_id_int = int(user_id[0])
        # sql = ('SELECT ticket_channel FROM guilds WHERE guild_id = ?')
        # val = (str(610914837039677471),)
        # await cursor.execute(sql,val)
        # channel_id = await cursor.fetchone()
        await cursor.close()
        await db.close()
        # channel = self.client.get_channel(int(channel_id[0]))
        # await ctx.message.user_id_int.send('someone responded to your ticket')
        # await channel.send(ticket_id)

    @ticket.command()
    async def status(self, ctx, ticket_id, *, content):
        "Change the status of a ticket"
        db = await aiosqlite.connect('marvin.db')
        cursor = await db.cursor()
        sql = ('UPDATE tickets SET status = ? WHERE ticket_id = ?')
        val = (str(content), str(ticket_id))
        await cursor.execute(sql,val)
        await cursor.close()
        await db.close()
        
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

import discord
import asyncpg
import asyncio
from apikeys import pgpswd
from datetime import datetime
from discord.ext import commands

class Tickets(commands.Cog, name="tickets"):
    """Ticket commands"""
    def __init__(self, client):
        self.client = client
        self.loop = asyncio.get_event_loop()
        self.credentials = 'postgresql://marvinclient:' + pgpswd + '@pgs-marvin-sfo2-1-do-user-4855641-0.db.ondigitalocean.com:25060/marvin?sslmode=require'

    @commands.group(invoke_without_command=True)
    async def ticket(self, ctx):
        connect = await asyncpg.connect(self.credentials)
        values = await connect.fetch('''SELECT * FROM guilds''')
        await ctx.send(values[0]['guild_id'])
        await connect.close()



    @commands.has_permissions(administrator=True)
    @ticket.command()
    async def panel(self, ctx, name=None):
        await ctx.send('new panel')


# edit embed to change color based on ticket status maybe
# add reactions to control ticket status and reponse
    @ticket.command()
    async def new(self, ctx, *, content):
        embed = discord.Embed(title="New Ticket - Ticket ID", colour=0x90ff)
        embed.add_field(name="Ticket author", value=f"{ctx.message.author}")
        embed.add_field(name="Content", value=f"{content}", inline=True)
        embed.add_field(name="Status", value="Open", inline=True)
        embed.add_field(name="Created", value=f"{datetime.now()}", inline=True)
        channel = self.client.get_channel(632070457302188034)
        await channel.send(embed=embed)

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

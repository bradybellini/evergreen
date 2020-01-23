import discord
import asyncio
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
        embed.add_field(name="Content", value=f"{content}", inline=False)
        embed.add_field(name="Status", value="Open", inline=False)
        embed.add_field(name="Response", value=f"none", inline=False)
        embed.add_field(name="Response by", value=f"none", inline=False)
        embed.add_field(name="Response Date", value=f"none", inline=False)
        embed.add_field(name="Created", value=f"{datetime.now()}", inline=False)
        channel = self.client.get_channel(669398602086613022)
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

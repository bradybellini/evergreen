import discord
from datetime import datetime
from discord.ext import commands

class Staff(commands.Cog, name='Staff commands'):
    """Staff related commands"""
    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @commands.group(invoke_without_command=True, hidden=True)
    async def staff(self, ctx):
        ": InfinityCraft 2.∞ Info for Staff"
        embed = discord.Embed(colour=0x74ff90, description="[] = required argument \n<> = optional argument ",)
        embed.set_author(name="InfinityCraft 2.∞ Staff Help")
        embed.add_field(
            name="Ticket Help", value=f"`m.staff tickets|ticket|t`", inline=False)
        embed.add_field(
            name="Moderation Help", value=f"`m.staff moderation|mod|m`", inline=False)
        embed.add_field(
            name="Important Links", value=f"`m.staff links|link|l`", inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(
            text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        await ctx.send(embed=embed)


    @commands.has_permissions(administrator=True)
    @staff.command(aliases=['link', 'l'])
    async def links(self, ctx):
        ": Important Links for Staff"
        embed = discord.Embed(colour=0x74ff90, description="",)
        embed.set_author(name="InfinityCraft 2.∞ Staff Links")
        embed.add_field(
            name="Important Links", value=f"Website: https://infinity.gamersgrove.net/ \nServer Server IP: mc.gamersgrove.net \nRaw IP: 208.87.97.11:25565 \nAdmin Panel: https://panel.gamersgrove.net/ \nRaw Panel IP: http://208.87.97.11:8080/", inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(
            text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        await ctx.send(embed=embed)


    @commands.has_permissions(administrator=True)
    @staff.command(aliases=['mod', 'm'])
    async def moderation(self, ctx):
        ": Staff Moderation Help"
        embed = discord.Embed(
            colour=0x74ff90, description="[] = required argument \n<> = optional argument ",)
        embed.set_author(name="InfinityCraft 2.∞ Moderation help")
        embed.add_field(
            name="Deleting Messages", value=f"`m.purge [amount]`", inline=False)
        embed.add_field(
            name="Kicking a User", value=f"`m.kick [user] <reason>`", inline=False)
        embed.add_field(
            name="Banning a User", value=f"`m.ban [user] <reason>`", inline=False)
        embed.add_field(
            name="Unbanning a User", value=f"`m.unban [user] <reason>`", inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(
            text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        await ctx.send(embed=embed)


    @commands.has_permissions(administrator=True)
    @staff.command(aliases=['ticket', 't'])
    async def tickets(self, ctx):
        ": Staff Ticket Help"
        embed = discord.Embed(
            colour=0x74ff90, description="[] = required argument \n<> = optional argument ",)
        embed.set_author(name="InfinityCraft 2.∞ Ticket help")
        embed.add_field(
            name="Respond to a Ticket", value=f"`m.ticket respond|reply|r [ticket id] [response]`", inline=False)
        embed.add_field(
            name="Change the Status of a Ticket", value=f"`m.ticket status [ticket id] [status]`", inline=False)
        embed.add_field(
            name="Search for a Ticket", value=f"_Coming soon_", inline=False)
        # : `m.ticket search|find [query]`
        embed.timestamp = datetime.utcnow()
        embed.set_footer(
            text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Staff(client))
    print('@COG: Staff Cog loaded \n---------------------')

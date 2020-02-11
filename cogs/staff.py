import discord
from datetime import datetime
from discord.ext import commands

class Staff(commands.Cog, name='Staff commands'):
    """Staff related commands"""
    def __init__(self, client):
        self.client = client

    # @commands.has_permissions(administrator=True)
    @commands.group(invoke_without_command=True)
    async def staff(self, ctx):
        ": InfinityCraft 2.∞ Info for Staff"


    @staff.commands()
    async def links(self, ctx):
        ": Important Links for Staff"
        embed = discord.Embed(colour=0x74ff90, description="```IP: mc.gamersgrove.net```",)
        embed.set_author(name="InfinityCraft 2.∞ Staff Help")
        embed.add_field(
            name="Important Links", value=f"Website: https://infinity.gamersgrove.net/ \nServer Server IP: mc.gamersgrove.net \nRaw IP: 208.87.97.11 \nAdmin Panel: https://panel.gamersgrove.net/ \nRaw Panel IP: http://208.87.97.11:8080/", inline=False)
        embed.add_field(
            name="Status", value=f"", inline=False)
        embed.add_field(name="Players", value=f"", inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(
            text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Staff(client))
    print('@COG: Staff Cog loaded \n---------------------')

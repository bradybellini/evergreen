import discord
import asyncio
import httpx
from datetime import datetime
from discord.ext import commands


class Minecraft(commands.Cog, name='Minecraft commands'):
    """Minecraft related commands"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 120, type=commands.BucketType.user)
    async def mojang(self, ctx):
        ": Details about the status of various Mojang and Minecraft services"
        async with httpx.AsyncClient() as client:
            r = await client.get('https://status.mojang.com/check')
        mcnet = r.json()[0]['minecraft.net']
        sessions = r.json()[1]['session.minecraft.net']
        account = r.json()[2]['account.mojang.com']
        auth = r.json()[3]['authserver.mojang.com']
        sessionserver = r.json()[4]['sessionserver.mojang.com']
        api = r.json()[5]['api.mojang.com']
        textures = r.json()[6]['textures.minecraft.net']
        mojang = r.json()[7]['mojang.com']
        embed = discord.Embed(colour=0x47814d)
        green = ':green_circle: No issues'
        orange = ':orange_circle: Some issues'
        red = ':red_circle: Service Unavailable'
        embed.set_author(name="Minecraft/Mojang Status",
                         url="https://status.mojang.com/check")
        embed.add_field(name="minecraft.net",
                        value=f"{green if mcnet == 'green' else orange if mcnet == 'yellow' else red}", inline=False)
        embed.add_field(name="session.minecraft.net",
                        value=f"{green if sessions =='green' else orange if sessions =='yellow' else red}", inline=False)
        embed.add_field(name="account.mojang.com",
                        value=f"{green if account =='green' else orange if account =='yellow' else red}", inline=False)
        embed.add_field(name="authserver.mojang.com",
                        value=f"{green if auth =='green' else orange if auth =='yellow' else red}", inline=False)
        embed.add_field(name="sessionserver.mojang.com",
                        value=f"{green if sessionserver =='green' else orange if sessionserver =='yellow' else red}", inline=False)
        embed.add_field(name="api.mojang.com",
                        value=f"{green if api =='green' else orange if api =='yellow' else red}")
        embed.add_field(name="textures.minecraft.net",
                        value=f"{green if textures =='green' else orange if textures =='yellow' else red}", inline=False)
        embed.add_field(
            name="mojang.com", value=f"{green if mojang =='green' else orange if mojang =='yellow' else red}", inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(
            text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        await ctx.send(embed=embed)

    @commands.group(invoke_without_command=True)
    async def server(self, ctx):
        ": Useful information about InfinityCrafy 2.∞"
        pass

    @server.command()
    async def ip(self, ctx):
        ": Shows the IP address for InfinityCrafy 2.∞"
        await ctx.send("```mc.gamersgrove.net```")

    @server.command()
    @commands.cooldown(1, 30, type=commands.BucketType.user)
    async def status(self, ctx):
        ": Get the current status of InfinityCraft 2.∞"
        async with httpx.AsyncClient() as client:
            r = await client.get('https://api.mcsrvstat.us/2/mc.gamersgrove.net')
        icon = 'https://api.mcsrvstat.us/icon/mc.gamersgrove.net'
        data = r.json()
        # players_online = ([players for players in data['players']['list']])
        players = (str(data['players']['online']) + '/' +
                   str(data['players']['max'])) if data['online'] == True else None
        embed = discord.Embed(
            colour=0x74ff90, description="```IP: mc.gamersgrove.net```",)
        embed.set_thumbnail(url=f"{icon}")
        embed.set_author(name="InfinityCraft 2.∞ Status",
                         url="http://mc.gamersgrove.net")
        embed.add_field(
            name="MOTD", value=f"{data['motd']['clean'][0] if data['online'] == True else None}", inline=False)
        embed.add_field(
            name="Status", value=f"{'Online' if data['online'] == True else 'Offline (Admins are aware, please do not ping)'}", inline=False)
        embed.add_field(name="Players", value=f"{players}", inline=False)
        # put on hold, list comprehension is having problems parsing thru json list or something. not high priority so whatever.
        # embed.add_field(name="Players Online", value=f"{players_online}", inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(
            text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        await ctx.send(embed=embed)

    # this is currently not working however it was working before on a different version of the api. It is def a jank way to do it (kinda) so might look into completely re making it
    @server.command(hidden=True)
    @commands.is_owner()
    async def autoreload(self, ctx):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            async with httpx.AsyncClient() as client:
                r = await client.get('https://api.mcsrvstat.us/2/mc.gamersgrove.net')
            icon = 'https://api.mcsrvstat.us/icon/mc.gamersgrove.net'
            data = r.json()
            embed = discord.Embed(colour=0x74ff90, url="https://discordapp.com",
                                  description="```IP: mc.gamersgrove.net```",)
            embed.set_thumbnail(url=f"{icon}")
            embed.set_author(name="InfinityCraft 2.∞ Status",
                             url="http://mc.gamersgrove.net")
            embed.add_field(
                name="MOTD", value=f"{data['motd']['clean'][0]}", inline=False)
            embed.add_field(
                name="Status", value=f"{'Online' if data['online'] == True else 'Offline (Admins are aware, please do not ping.)'}", inline=False)
            embed.add_field(
                name="Players", value=f"{data['players']['online']}/{data['players']['max']}", inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text="Last Updated ->")
            message = await self.client.get_channel(672336514679832578).fetch_message(672339911952564234)
            await message.edit(embed=embed)
            await asyncio.sleep(60)

    @mojang.error
    @status.error
    async def status_error(self, ctx, error):
        embed = discord.Embed(
            title=f" Try again in {int(error.retry_after)} seconds.", colour=0xd95454)
        embed.set_author(name=f"You are on a cooldown for this command!")
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Minecraft(client))
    print('@COG: Minecraft Cog loaded \n---------------------')

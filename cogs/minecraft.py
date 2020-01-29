import discord
import asyncio
import httpx
import datetime
from discord.ext import commands

class Minecraft(commands.Cog, name='Minecraft commands'):
    """Minecraft related commands"""
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def mojang(self, ctx):
        "Details about the status of various Mojang and Minecraft services"
        async with httpx.AsyncClient() as client:
            r = await client.get('https://status.mojang.com/check')
        mcnet = r.json()[0]['minecraft.net']
        sessions = mcnet = r.json()[1]['session.minecraft.net']
        account = mcnet = r.json()[2]['account.mojang.com']
        auth = mcnet = r.json()[3]['authserver.mojang.com']
        sessionserver = mcnet = r.json()[4]['sessionserver.mojang.com']
        api = mcnet = r.json()[5]['api.mojang.com']
        textures = mcnet = r.json()[6]['textures.minecraft.net']
        mojang = mcnet = r.json()[7]['mojang.com']
        embed = discord.Embed(colour=0x47814d)
        green = ':green_circle: No issues'
        orange = ':orange_circle: Some issues'
        red = ':red_circle: Service Unavailable'
        embed.set_author(name="Minecraft/Mojang Status", url="https://status.mojang.com/check")
        embed.add_field(name="minecraft.net", value=f"{green if mcnet == 'green' else orange if mcnet == 'yellow' else red}", inline=False)
        embed.add_field(name="session.minecraft.net", value=f"{green if sessions =='green' else orange if sessions =='yellow' else red}", inline=False)
        embed.add_field(name="account.mojang.com", value=f"{green if account =='green' else orange if account =='yellow' else red}", inline=False)
        embed.add_field(name="authserver.mojang.com", value=f"{green if auth =='green' else orange if auth =='yellow' else red}", inline=False)
        embed.add_field(name="sessionserver.mojang.com", value=f"{green if sessionserver =='green' else orange if sessionserver =='yellow' else red}", inline=False)
        embed.add_field(name="api.mojang.com", value=f"{green if api =='green' else orange if api =='yellow' else red}")
        embed.add_field(name="textures.minecraft.net", value=f"{green if textures =='green' else orange if textures =='yellow' else red}", inline=False)
        embed.add_field(name="minecraft.net", value=f"{green if mojang =='green' else orange if mojang =='yellow' else red}", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        await ctx.send(embed=embed)



    @commands.group(invoke_without_command=True)
    async def server(self, ctx):
        pass

    @server.command()
    async def status(self, ctx):
        pass

    @server.command()
    async def list(self, ctx):
        pass
 

def setup(client):
    client.add_cog(Minecraft(client))
    print('@COG: Minecraft Cog loaded \n---------------------')

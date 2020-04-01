import discord
import base64
import paramiko
import asyncio
import httpx
from apikeys import ssh_secret, ssh_pass, ssh_user, ssh_ip, amp_pass, amp_url_base, amp_user
from discord.ext import commands


class Backend(commands.Cog, name="Server sided stuff"):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @commands.command(hidden=True)
    @commands.cooldown(1, 600, type=commands.BucketType.guild)
    async def backup(self, ctx):
        key = paramiko.ECDSAKey(data=base64.b64decode(f'{ssh_secret}'))
        try:
            client = paramiko.SSHClient()
            client.get_host_keys().add(f'{ssh_ip}', 'ssh-rsa', key)
            client.connect(f'{ssh_ip}', username=f'{ssh_user}',
                        password=f'{ssh_pass}')
            await ctx.send("Backup has started.")
            client.exec_command('./scripts/backup_infinitycraft.sh')
            await asyncio.sleep(180)
            # may need to bump up later or find a way to see when its done
        except:
            await ctx.send("Backup failed to start or connect to host server.")
        client.close()

    @commands.has_permissions(administrator=True)
    @commands.group(invoke_without_command=True, hidden=True)
    @commands.cooldown(1, 5, type=commands.BucketType.user)
    async def console(self,ctx):
        pass

    @commands.has_permissions(administrator=True)
    @console.command()
    @commands.cooldown(1, 5, type=commands.BucketType.user)
    async def send(self, ctx, *, command):
        headers = {
            'Accept': 'application/json, text/javascript',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        url = amp_url_base + 'Login'
        data = str({"username":f"{amp_user}","password":f"{amp_pass}","token":"","rememberMe":"true","SESSIONID":""})
        async with httpx.AsyncClient() as client:
            r = await client.post(url, headers=headers, data=data)

            url = amp_url_base + 'SendConsoleMessage'
            data = str({"message":f"""{command}""","SESSIONID": f"{r.json()['sessionID']}"})
            r = await client.post(url, headers=headers, data=data)
            print(r.json())


    @backup.error
    async def backup_error(self, ctx, error):
        embed = discord.Embed(
            title=f" Try again in {int(error.retry_after)} seconds.", colour=0xd95454)
        embed.set_author(name=f"You are on a cooldown for this command!")
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Backend(client))
    print('@COG: Meta Cog loaded \n---------------------')

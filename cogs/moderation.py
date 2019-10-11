import discord
from discord.ext import commands

class Moderation(commands.Cog, name='Moderation Commands'):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def purge(self, ctx, amount:int):
        deleted = await ctx.message.channel.purge(limit=amount + 1)
        await ctx.send(f'Messages deleted by {ctx.message.author.mention}: `{len(deleted)}`')

    @purge.error
    async def purge_error(self, ctx, error):
        embed = discord.Embed(title="Try: m.purge [message amount]", colour=0xd95454)
        embed.set_author(name=f"{error}", url="https://discordapp.com")
        embed_badarg = discord.Embed(title="Try: m.purge [message amount]", colour=0xd95454)
        embed_badarg.set_author(name="Message amount must be a number.", url="https://discordapp.com")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            await ctx.send(embed=embed_badarg)

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, user:discord.Member, *, reason=None):
        if not reason:
            await ctx.guild.kick(user=user, reason='No reason provided')
            # insert embed with user kicked and reason for kicking
        else:
            await ctx.guild.kick(user=user, reason=reason)
            # insert embed with user kicked and reason for kicking

    @kick.error
    async def kick_error(self, ctx, error):
        # add error for trying to kick someone of equal or greater permissions and thats it for perms
        embed = discord.Embed(title="Try: m.kick [user] <reason>", colour=0xd95454)
        embed.set_author(name=f"{error}", url="https://discordapp.com")
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, user:discord.Member, *, reason=None):
        await ctx.guild.ban(user=user, reason=reason)
        await ctx.send(f'{user} has been banned')


    @ban.error
    async def ban_error(self, ctx, error):
        # add error for trying to banning someone of equal or greater permissions and thats it for perms
        embed = discord.Embed(title="Try: m.ban [user] <reason>", colour=0xd95454)
        embed.set_author(name=f"{error}", url="https://discordapp.com")
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
    print('@COG: Moderation Cog loaded \n---------------------')
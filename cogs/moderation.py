import discord
from discord.ext import commands

class Moderation(commands.Cog, name='Moderation Commands'):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def purge(self, ctx, *, amount:int=None):
        try:
            if not amount:
                # add default error embed here
                await ctx.send('User must specify the number of messages for Marvin to delete')
            else:
                deleted = await ctx.message.channel.purge(limit=amount)
                await ctx.send(f'Messages deleted by {ctx.message.author.mention}: `{len(deleted)}`')
        except:
            await ctx.send('Marvin can not purge messages here.')

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

def setup(client):
    client.add_cog(Moderation(client))
    print('@COG: Moderation Cog loaded \n---------------------')
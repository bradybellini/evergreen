import discord
from discord.ext import commands

class Moderation(commands.Cog, name='Moderation Commands'):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def purge(self, ctx, *, amount:int=None):
        try:
            if amount is None:
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
            # Add in missing required arg error for user
        if user.guild_permissions.kick_members:
            if not reason:
                await ctx.guild.kick(user=user, reason='No reason provided')
                # insert embed with user kicked and reason for kicking
            else:
                await ctx.guild.kick(user=user, reason=reason)
                # insert embed with user kicked and reason for kicking
        else:
            pass
            # error embed saying that the user has equal or more permission than then so they cannot kick them


def setup(client):
    client.add_cog(Moderation(client))
    print('@COG: Moderation Cog loaded \n---------------------')
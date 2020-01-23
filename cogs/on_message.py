import discord
import datetime
from discord import Message, TextChannel, Member, PartialEmoji
from discord.ext import commands


class OnMessage(commands.Cog, name='On Message Listeners and Events'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(error)

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.author == self.client.user.id: #or message.author.guild_permissions.manage_messages:
            return
        
        if message.content.startswith('m.report') and message.channel.type == discord.ChannelType.text:
            await message.delete()
            await message.channel.send(f'{message.author.mention} Reports must be made in a DM with Marvin')


def setup(client):
    client.add_cog(OnMessage(client))
    print('@EVENT: OnMessage Event loaded \n---------------------')

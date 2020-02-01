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
        # if discord.ChannelType.private:
        #     return
            
        if message.author == self.client.user.id or message.author.guild_permissions.manage_messages:
            return
        
        if message.content.startswith('m.ticket ') and message.channel.type == discord.ChannelType.text:
            await message.delete()
            await message.channel.send(f'{message.author.mention} Your ticket has been submitted, if you did not receive a DM from Marvin, let a staff member know.')


def setup(client):
    client.add_cog(OnMessage(client))
    print('@EVENT: OnMessage Event loaded \n---------------------')

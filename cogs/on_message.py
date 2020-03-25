import discord
from discord import Message, TextChannel, Member
from discord.ext import commands


class OnMessage(commands.Cog, name='On Message Listeners and Events'):

    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     await ctx.send(error)

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if discord.ChannelType.private:
            return

        if self.client.user.id or message.author.guild_permissions.manage_messages:
            return

        # and message.channel.type == discord.ChannelType.text:
        if message.content.startswith('m.ticket ') or message.content.startswith('m.report '):
            await message.delete()
            await message.channel.send(f'{message.author.mention} Your ticket has been submitted, if you did not receive a DM from Marvin, let a staff member know. Please submit tickets and reports in a direct message with {self.client.mention} from now on.')
# 

def setup(client):
    client.add_cog(OnMessage(client))
    print('@EVENT: OnMessage Event loaded \n---------------------')

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
            await  message.delete()
            await message.channel.send(f'{message.author.mention} Your ticket has been submitted, if you did not receive a DM from Marvin, let a staff member know. Please submit tickets and reports in a direct message with {self.client.user.mention} from now on.'),       # 

        if message.content.contains('link discord') and message.channel == self.client.get_channel(623702240523321356):
            help_channel: TextChannel = self.client.get_channel(
                623702240523321356)
            await message.help_channel.send(f'If you would like to link your Discord and Minecraft account to get the Voyager rank, type `/discord link` in **Minecraft**. You will be given a code which you will need to send in a direct message to Eve. It can take up to 5 minutes for the rank to sync, so please be patient.')
        
def setup(client):
    client.add_cog(OnMessage(client))
    print('@EVENT: OnMessage Event loaded \n---------------------')

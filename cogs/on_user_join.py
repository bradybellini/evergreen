import discord
from discord import Message, TextChannel, Member
from discord.ext import commands


class OnMemberJoin(commands.Cog, name='On Member Join Listeners and Events'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        help_channel: TextChannel = self.client.get_channel(623702240523321356)
        ticket_channel: TextChannel = self.client.get_channel(
            673097926825738250)
        rules_channel: TextChannel = self.client.get_channel(
            622988649113583637)
        join_message = f""":small_orange_diamond: Welcome to InfinityCraft 2.∞! If you need help make sure to check out the {help_channel.mention} channel or run the command `m.help` to get Marvin(me) to give you command help within the server. 
:small_orange_diamond: I may take some time to respond to your command so please be patient. I am a cactus after all. 
:small_blue_diamond: Make sure to run the command `/discord link` in Minecraft to link your Minecraft and Discord account and follow the directions given. You should get the Voyager rank as well as some other perks. 
:small_blue_diamond: To submit a report or ticket, check out the {ticket_channel.mention} channel. 
:small_blue_diamond: Last of all, make sure to follow all the rules posted in the {rules_channel.mention} channel. You can also use the command `m.rules` to view all of the rules. 
:small_blue_diamond: If you have any further questions, feel free to ask a staff member or other members of the community.

Server IP: `mc.playinfinitycraft.com`
Website: https://infinity.gamersgrove.net/
Discord Invite Link: https://discordapp.com/invite/v67aGnq"""
        await member.send(join_message)


def setup(client):
    client.add_cog(OnMemberJoin(client))
    print('@EVENT: OnMemberJoin Event loaded \n---------------------')

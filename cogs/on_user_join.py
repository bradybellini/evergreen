import discord
from datetime import datetime
from discord import Message, TextChannel, Member
from discord.ext import commands


class OnMemberJoin(commands.Cog, name='On Member Join Listeners and Events'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        join_message = "Welcome! If you need help make sure to check out the #help channel or run the command `m.help` to get Marvin(me) to give you command help within the server. I may take some time to responde to your command so please be patient. I am a cactus after all. Make sure to run the command `/discord link` in Minecraft to link your Minecraft and discord account and follow the directions given. You should get the Voyager rank as well as some other perks. To submit a report or ticket, check out the #ticket channel. Last of all, make sure to follow all the rules posted in the #rules channel. If you have any further questions, feel free to ask a staff member or other members of the community."
        await member.send(join_message)


def setup(client):
    client.add_cog(OnMemberJoin(client))
    print('@EVENT: OnMemberJoin Event loaded \n---------------------')

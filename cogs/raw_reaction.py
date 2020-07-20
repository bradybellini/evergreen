import discord
import asyncio
import aiosqlite
from datetime import datetime
from discord import Message, TextChannel, Member, PartialEmoji
from discord.ext import commands


class OnRawReaction(commands.Cog, name='On Raw Reaction Listeners and Events'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload:discord.RawReactionActionEvent):
        if payload.user_id == self.client.user.id:
            return

        report_embed = discord.Embed(colour=0xff6363, description="Before you report someone, please consider the following:\n:small_orange_diamond: Does a staff member need to be involved?\n:small_orange_diamond: Did the person explicitly break any of the rules?\n\n:octagonal_sign: If you answered no to any of the above questions, please try and resolve the problem on your own before submitting a report.")
        report_embed.set_author(name="Report a Player or Staff", icon_url="https://i.imgur.com/sjHfdUg.png")
        report_embed.set_footer(text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        report_embed.timestamp = datetime.utcnow()
        report_embed.add_field(name="What to include in the report?", value=":small_blue_diamond: Please include your minecraft username (We will have your Discord name from the report)\n:small_blue_diamond: Any proof you have, i.e screenshots.\n:small_blue_diamond: An explanation of what happend and who was involved. Please include both minecraft usernames AND discord usernames if possible.\n:small_blue_diamond: Any other information that you would otherwise deem useful for this case.", inline=False)
        report_embed.add_field(name="Other Information", value=":question:Marvin will give you  a ticket number. Please keep track of this number as it will be the easiest way for a staff member to reference the ticket.\n:question:Please only submit ONE report. If multiple reports are created for the same situation, you could risk your report being ignore. We see all reports and will get back to you as soon as possible.\n:question: Please upload the screenshots to an image sharing website like [Imgur](https://imgur.com/) or [ImageBB](https://imgbb.com/) and include the link in the report. Marvin cannot store image files in his database, so any picture you upload directly to discord will be ignored.", inline=False)
        report_embed.add_field(name="Command", value="To submit a report, type `m.report new [report]`\nReplace `[report]` with your report including all information you need to include in ONE message.", inline=False)
   
        new_ticket_embed = discord.Embed(colour=0x3981ff, description="The ticket you submit should not include a player or staff report. Please go back to the help module if you want to report a player or staff member.")
        new_ticket_embed.set_author(name="Help Ticket", icon_url="https://i.imgur.com/YeeBFpu.png")
        new_ticket_embed.set_footer(text="Marvin", icon_url=f'{self.client.user.avatar_url}')
        new_ticket_embed.timestamp = datetime.utcnow()
        new_ticket_embed.add_field(name="Reasons to submit a help ticket", value=":small_blue_diamond: You bought a donor rank or a crate key and you did not receive it\n:small_blue_diamond: A technial problem or glitch with an in-game feature or plugin\n:small_blue_diamond: Other technical issues not mentioned", inline=False)
        new_ticket_embed.add_field(name="Technical Problems", value="If the problem does not directly involve InfinityCraft 2.∞ services, i.e. our Minecraft server, Discord, or Website, there is no guarantee we will be able to solve or help you with your problem.", inline=False)
        new_ticket_embed.add_field(name="Other Information", value=":question:Marvin will give you a ticket number. Please keep track of this number as it will be the easiest way for a staff member to reference the ticket.\n:question:Please only submit ONE ticket. If multiple tickets are created for the same issue, you could risk your ticket being ignore. We see all tickets and will get back to you as soon as possible.\n:question: If needed, please upload screenshots to an image sharing website like [Imgur](https://imgur.com/) or [ImageBB](https://imgbb.com/) and include the link in the ticket. Marvin cannot store image files in his database, so any picture you upload directly to discord will be ignored.", inline=False)
        new_ticket_embed.add_field(name="Command", value="To submit a new ticket, type `m.ticket new [message]`\nReplace `[message]` with your message including all information you need to include in ONE message.")
 
        db = await aiosqlite.connect('marvin.db')
        cursor = await db.cursor()
        sql = ("SELECT ticket_panel FROM guilds WHERE guild_id = ?")
        val = (str(610914837039677471),)
        await cursor.execute(sql,val)
        message_id = await cursor.fetchone()
        await cursor.close()
        await db.close()
        channel:TextChannel = self.client.get_channel(payload.channel_id)
        message:Message = await channel.fetch_message(payload.message_id)
        member:Member = self.client.get_guild(payload.guild_id).get_member(payload.user_id)
        emoji:PartialEmoji = payload.emoji

        if message_id is None:
            return
        else:
            message_id_db = int(message_id[0])

        if emoji.name == '⛔' and payload.message_id == message_id_db:
            await member.send(embed=report_embed)
            await message.remove_reaction(emoji, member)
        elif emoji.name == '🎟' and payload.message_id == message_id_db:
            await member.send(embed=new_ticket_embed)
            await message.remove_reaction(emoji, member)

        if payload.user_id == self.client.user.id or payload.message_id != message_id_db:
            return 
        else:
            await message.remove_reaction(emoji, member)


def setup(client):
    client.add_cog(OnRawReaction(client))
    print('@EVENT: OnRawReaction Event loaded \n---------------------')
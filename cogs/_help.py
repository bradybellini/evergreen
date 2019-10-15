import discord
from discord.ext import commands

class Help(commands.Cog, name="help"):
    """Help me!"""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Visit hellomarvin.org for more help and info.", colour=0xc91fe5, url="https://discordapp.com", 
        description="""```asciidoc
= Hello, I am Marvin. I look forward to your company. =
= Please visit hellomarvin.org for further help       =

meta::
  ping  : Check latency to Marvin
moderation::
  ban   : Ban a user
  kick  : Kick a user
  purge : Deletes specified amount of messages
  unban : Unban a user
No Category::
  help  : Shows this message

= Type m.help <command> for more info on a command.   =
= You can also type m.help <category> for more info.  =

```""")
        embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
    print('@COG: Help Cog loaded \n---------------------')
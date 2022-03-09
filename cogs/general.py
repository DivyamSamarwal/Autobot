import discord
import datetime
from datetime import datetime
from discord.ext import commands
datetime.utcnow()
import random

class General(commands.Cog, name='General'):
    """General commands"""

    def __init__(self,bot):
        self.bot = bot


    
    @commands.command(aliases=['latency'])
    async def ping(self,ctx):
        embed = discord.Embed(title="Pong!",description=f'{round(self.bot.latency *1000)}ms',color=discord.Color.random(),timestamp=datetime.utcnow())

        await ctx.send(embed=embed)    

    @commands.command(aliases=['8ball', '8b'])
    async def Eightball(self,ctx, *, ques):
        responses = [
            "As I see it, yes.", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.",
            "Don’t count on it.", "It is certain.", "It is decidedly so.",
            "Most likely.", "My reply is no.", "My sources say no.",
            "Outlook not so good.", "Outlook good.", "Reply hazy, try again.",
            "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.",
            "Yes – definitely.", "You may rely on it.", "*hmm*"]
        embed = discord.Embed(title=" 🎱8ball ",
                          description="Questions and Answers",
                          color=discord.Color.random())
        embed.add_field(name="Question", value=f'{ques}', inline=False)
        embed.add_field(name="Answer",
                    value=f'{random.choice(responses)}',
                    inline=False)

        await ctx.send(embed=embed)    

    @commands.command()
    async def imagine(self,ctx):
        responses = [
        "https://media.discordapp.net/attachments/862895445381218334/871692994955329567/My_Post.png?width=1078&height=606",
        "https://media.discordapp.net/attachments/862895445381218334/871698288053723136/My_Post_1.png?width=1078&height=606",
        "https://media.discordapp.net/attachments/862895445381218334/871710199931621396/My_Post_2.png?width=1078&height=606"]
        message = await ctx.send(' `Imagining...`')
        await message.edit(content=" `10% complete`")
        await message.edit(content=" `50% complete`")
        await message.edit(content=" `100% complete`")
        await message.edit(content=f' {random.choice(responses)}')

def setup(client):
    client.add_cog(General(client))
    print("General cog is Loaded!")
    

import discord
import datetime
from datetime import datetime
from discord.ext import commands
datetime.utcnow()


class General(commands.Cog, name='General'):
    """General commands"""

    def __init__(self,bot):
        self.bot = bot


    
    @commands.command(aliases=['latency'])
    async def ping(self,ctx):
        embed = discord.Embed(title="Pong!",description=f'{round(self.bot.latency *1000)}ms',color=discord.Color.random(),timestamp=datetime.utcnow())

        await ctx.send(embed=embed)    


def setup(client):
    client.add_cog(General(client))
    print("General cog is Loaded!")
    

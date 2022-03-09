import discord
import datetime
from datetime import datetime
from discord.ext import commands
from aiohttp import request
datetime.utcnow()
import asyncio
import googletrans
from googletrans import Translator
class Utility(commands.Cog, name='Utility'):
    """Utility commands"""

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def slowmode(self,ctx,time:int):
        if (not ctx.author.guild_permissions.manage_messages):
            embed = discord.Embed(title="Permission error" , description="This requires `Manage Message Permission`.You don't have that!",color=discord.Colour.dark_red())
            await ctx.send(embed=embed)
            return
        try:
            if time == 0:
                embed1 = discord.Embed(title="Slowmode succesfully off", description="If time has been set to 0 seconds then slowmode would be off. <a:tick:940195528103325726>",color=discord.Colour.dark_teal())
                await ctx.send(embed=embed1)
                await ctx.channel.edit(slowmode_delay = 0)
            elif time > 21600:
                emb = discord.Embed(title="Time Error <a:wrong:940200609326444594>" , description="You can not set the slowmode above `6 hours`",color=discord.Colour.red())
                emb.add_field(name="Quick Conversions", value="1 min =  60 seconds \n 2 min = 120 seconds \n 5 min = 300 seconds \n 1 hour = 3600 seconds \n 6 hours = 21600 seconds")
                await ctx.send(embed=emb)
                return
            else:
                await ctx.channel.edit(slowmode_delay = time)
                em = discord.Embed(title="Succesfully set! <a:tick:940195528103325726>", description=f"Slowmode set to {time} seconds" , color= discord.Colour.teal())
                await ctx.send(embed=em)
        except Exception:
            await print("Oops!")
#polls


    @commands.command(pass_context=True)
    async def poll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), color=discord.Colour.random())
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await react_message.edit(embed=embed)

    @commands.command(pass_context=True)
    async def tally(self, ctx, id=None):
        poll_message = await ctx.channel.fetch_message(id)
        embed = poll_message.embeds[0]
        unformatted_options = [x.strip() for x in embed.description.split('\n')]
        print(f'unformatted{unformatted_options}')
        opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
            else {x[:1]: x[2:] for x in unformatted_options}
        # check if we're using numbers for the poll, or x/checkmark, parse accordingly
        voters = [self.bot.user.id]  # add the bot's ID to the list of voters to exclude it's votes

        tally = {x: 0 for x in opt_dict.keys()}
        for reaction in poll_message.reactions:
            if reaction.emoji in opt_dict.keys():
                reactors = await reaction.users().flatten()
                for reactor in reactors:
                    if reactor.id not in voters:
                        tally[reaction.emoji] += 1
                        voters.append(reactor.id)
        output = f"Results of the poll for **{embed.title}** :\n" + '\n'.join(['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
        await ctx.send(output)

    @commands.command()
    async def math(self,ctx, *, expression:str):
        calculation = eval(expression)
        embed=discord.Embed(title="Math",description='Math: {}\nAnswer: {}'.format(expression, calculation),color=discord.Colour.random(), timestamp=datetime.utcnow())
        await ctx.send(embed=embed)   

    @commands.command(aliases=["translate","tl"])
    async def trans(self,ctx, lang, *, thing):
        embed = discord.Embed(title="Translator🔎",description="Translates from inputed language to which you want..",
        color=discord.Color.random(),
        timestamp=datetime.utcnow())
        translator = Translator()
        translation = translator.translate(thing, dest=lang)
        embed.add_field(name="Inputed text", value=thing, inline=False)
        embed.add_field(name="Translated text",
                    value=translation.text,
                    inline=False)
        await ctx.reply(embed=embed)
    @trans.error
    async def trans_error(self,ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(title="API Error",
            description=
            "API => `googletrans==3.1.0a0` invoked so many errors that bot owner got tired while solving and broke the hosting server caused so much damage.\n Help us in recovering damage.\n https://www.patreon.com/AutoBot0521",
            colour=discord.Colour.random(),
            timestamp=datetime.utcnow())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/906314638428348528.gif?size=56&quality=lossless")    
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Utility(client))
    print("Utility cog is Loaded!")


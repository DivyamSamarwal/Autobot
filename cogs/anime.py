import discord
import animec
import datetime
from datetime import datetime
from discord.ext import commands
from aiohttp import request

class Anime(commands.Cog, name='Anime'):
    """Anime commands for weebs"""

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def anime(self,ctx,*,query):
        try:
            anime = animec.Anime(query)
        except:
            await ctx.send(embed = discord.Embed(description="No corresponding Anime is found for the search query",color=discord.Colour.red()))
            return 
        embed=discord.Embed(title=anime.title_english,url=anime.url,description=f'{anime.description[:300]}.....',color = discord.Colour.random())
        embed.add_field(name = "Episodes",value=str(anime.episodes))
        embed.add_field(name = "Rating",value=str(anime.rating))
        embed.add_field(name = "Aired",value=str(anime.aired))
        embed.add_field(name = "Ranked",value=str(anime.ranked))
        embed.add_field(name = "Popularity",value=str(anime.popularity))
        embed.add_field(name = "Favourites",value=str(anime.favorites))
        embed.add_field(name = "Broadcast",value=str(anime.broadcast))
        embed.add_field(name = "Status",value=str(anime.status))
        embed.add_field(name = "Type",value=str(anime.type))
        embed.add_field(name = "Name of the anime in japanese",value=str(anime.title_jp))
        embed.add_field(name = "The Anime is also known as",value=str(anime.alt_titles))
        embed.add_field(name = "Producers",value=list(anime.producers))
        embed.add_field(name = "Genres",value=list(anime.genres))
        embed.add_field(name = "Teaser",value=str(anime.teaser))
        embed.add_field(name = "Recommend",value=list(anime.recommend()))
        embed.add_field(name = "NSFW status",value=str(anime.is_nsfw()))
        embed.set_thumbnail(url=anime.poster)
        await ctx.send(embed=embed)

    @commands.command(aliases=["char","animecharacter"])
    async def character(self,ctx,*,query):
        try:
            char = animec.Charsearch(query)
        except:
            await ctx.send(embed = discord.Embed(description="No corresponding Anime Character is found for the search query",color=discord.Colour.red()))
            return 
        embed=discord.Embed(title=char.title,url=char.url,color = discord.Colour.random())
        embed.set_image(url=char.image_url)
        embed.set_footer(text=", ".join(list(char.references.keys())[:2]))
        await ctx.send(embed = embed)

    @commands.command(aliases=["aninews"])
    async def animenews(self,ctx,amount:int=3):
        news = animec.Aninews(amount)
        links = news.links
        titles=news.titles
        descriptions = news.description

        embed= discord.Embed(title = "Latest Anime News",color=discord.Colour.random(),timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=news.images[0])

        for  i in  range (amount):
            embed.add_field(name= f"{i+1}) {titles[i]}", value=f"{descriptions[i][:200]}...\n[Read more]({links[i]})",inline=False)
        await ctx.send(embed = embed)




    @commands.command(name="pat", aliases=['pats', 'headpat', 'headpats'])
 
    async def pat_(self, ctx: commands.Context, user: discord.Member):
        """Pat someone"""
        if user.bot:
            return await ctx.send(embed=discord.Embed(description="** <a:wrong:940200609326444594> You can't pat a bot.**", color=discord.Colour.red()))
        if user == ctx.author:
            return await ctx.send(embed=discord.Embed(description="**<a:wrong:940200609326444594> You can't pat yourself! Try patting someone else.**", color=discord.Colour.red()))

        url = "https://some-random-api.ml/animu/pat"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed= discord.Embed(description=f'{ctx.author.mention} patted {user.mention}',color=discord.Colour.green())
                embed.set_image(url=data['link'])
                await ctx.send(embed=embed)
                
            else:
                embed = discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed)
                #await ctx.send(f"API ERRORS {response.status}status.")


    @commands.command(name="hug", aliases=['hugs', 'backhug', 'chesthugs'])
   
    async def hug_(self, ctx: commands.Context, user: discord.Member):
        """Hug someone"""
        if user.bot:
            return await ctx.send(embed=discord.Embed(description="**<a:wrong:940200609326444594> You can't hug a bot.**", color=discord.Colour.red()))
        if user == ctx.author:
            return await ctx.send(embed=discord.Embed(description="**<a:wrong:940200609326444594> You can't hug yourself! Try hugging someone else.**", color=discord.Colour.red()))

        url = "https://some-random-api.ml/animu/hug"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed = discord.Embed(description=f"{ctx.author.mention} hugs {user.mention}",color=discord.Colour.green())
                embed.set_image(url=data['link'])
                await ctx.send(embed=embed)
            else:
                embed= discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed)               
                #await ctx.send(f"API ERRORS {response.status}status.")


    @commands.command(name="slap")
    async def slap_(self, ctx: commands.Context, user: discord.Member):
        """Slap someone"""
        if user.bot:
            return await ctx.send(embed=discord.Embed(description="**<a:wrong:940200609326444594> You can't slap a bot.**", color=discord.Colour.red()))
        if user == ctx.author:
            return await ctx.send(embed=discord.Embed(description="**<a:wrong:940200609326444594> You can't slap yourself! Try slapping someone else.**", color=discord.Colour.red()))

        url = "https://neko-love.xyz/api/v1/slap"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed = discord.Embed(description=f"{ctx.author.mention} slaps {user.mention}",color=discord.Colour.green())
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
            else:
                embed= discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed)               
                #await ctx.send(f"API ERRORS {response.status}status.")
    
    @commands.command(name="wink")

    async def wink_(self, ctx: commands.Context):
        """wink your eye"""
        

        url = "https://api.waifu.pics/sfw/wink"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed = discord.Embed(description=f"{ctx.author.mention} Your wink is unique",color=discord.Colour.green())
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
            else:
                embed= discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed)               
                #await ctx.send(f"API ERRORS {response.status}status.")

    @commands.command(name="bully")

    async def bully_(self, ctx: commands.Context, user: discord.Member):
        """Bully Someone"""
        

        url = "https://api.waifu.pics/sfw/bully"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed = discord.Embed(description=f"{ctx.author.mention} bullies {user.mention}",color=discord.Colour.green())
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
            else:
                embed= discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed) 


    @commands.command(name="cuddle")
    async def cuddle_(self, ctx: commands.Context, user: discord.Member):
        """Cuddle Someone"""
        

        url = "https://api.waifu.pics/sfw/cuddle"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed = discord.Embed(description=f"{ctx.author.mention} cuddles {user.mention}",color=discord.Colour.green())
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
            else:
                embed= discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed)



    @commands.command(name="cry")
    async def cry_(self, ctx: commands.Context, * , reason=None):
        """Anime Cry for something"""
        

        url = "https://api.waifu.pics/sfw/cry"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed = discord.Embed(description=f"{ctx.author.mention} is crying for \n reason : **{reason}**",color=discord.Colour.green())
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
            else:
                embed= discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed)


    @commands.command(name="kiss")

    async def kiss_(self, ctx: commands.Context, user: discord.Member):
        """Kiss someone"""
        

        url = "https://api.waifu.pics/sfw/kiss"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed = discord.Embed(description=f"{ctx.author.mention} kisses {user.mention}",color=discord.Colour.green())
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
            else:
                embed= discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed)
                
    @commands.command(name="waifu")
    async def waifu(self, ctx: commands.Context, * , reason=None):
        """Waifu"""


        url = "https://api.waifu.pics/sfw/waifu"
        async with request("GET", url, headers={}) as response:
            if response.status == 200:
                data = await  response.json()
                embed = discord.Embed(description=f"<:keqing:939052537699512340> Requested by {ctx.author.name}",color=discord.Colour.random(),timestamp=datetime.utcnow())
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
            else:
                embed= discord.Embed(description=f"API ERRORS {response.status}status.",color=discord.Colour.red())
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Anime(client))
    print("Anime cog is Loaded!")
    

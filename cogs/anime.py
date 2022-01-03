import discord
import animec
import datetime
from discord.ext import commands

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
    async def image(self,ctx,*,query):
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



       
def setup(client):
    client.add_cog(Anime(client))
    print("Anime cog is Loaded!")

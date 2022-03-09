from asyncio.tasks import wait
from http import server
from time import time
from typing import Optional
import discord
import random
from discord import Guild, colour
from discord import embeds
from discord import message
from discord import role
from discord.client import Client
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands, tasks
from discord.ext.commands import is_owner
from random import choice
import datetime
import asyncio
from discord import DefaultAvatar

import googletrans
from googletrans import Translator
from urllib import parse, request
import re
from datetime import timedelta
from datetime import datetime
from discord.ext.commands.converter import clean_content

from discord.ext.commands.core import command
from discord import Message
import json
from discord import Client, Intents, Embed
from discord import Client, Intents, Embed
from discord_slash import SlashCommand
from typing import Union
import math

from sqlalchemy import desc
from webserver import keep_alive
import sys
import traceback
import os
from aiohttp import request
import akinator
from discord.ext import commands
from akinator.async_aki import Akinator

from discord.ext.commands import BucketType
import requests
import aiohttp
intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(commands.when_mentioned_or('&'),intents=intents,case_insensitive=True)
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name=f'/help | &help'))
    print(' Hello I am AutoBot. ')
    client.load_extension('dismusic')
    client.load_extension('jishaku')


     
#on_guild_join
@client.event
async def on_guild_join(guild):
    try:
        channel = guild.system_channel
        em = discord.Embed(title = "Thanks for adding AutoBot#0521", description = "You can also add my friend **Terra#0969**, it plays 24*7 music(Youtube|Spotify|Soundcloud) [here](https://discord.com/oauth2/authorize?client_id=866674108489269288&permissions=2205281600&scope=bot%20identify%20guilds%20applications.commands&redirect_url=https://divyamsamarwal.wixsite.com/autobot/api/callback&response_type=code)", colour=discord.Color.random(), timestamp=datetime.utcnow())
        em.add_field(name="Config", value="My default prefix is **&** or **when_mentioned** <@!858965828716331019> \n You can type **&help** and get all the useful commands. \n Please make sure I have **Administrator** permissions so that every command can use be used without a problem.", inline=False)
        em.set_thumbnail(url="https://images-ext-1.discordapp.net/external/2PV16r98prv5VZyrJ8WL0usihP-cVCnw4FXAUbhtEwU/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/858965828716331019/9d6df6a23acdf3b54f96168ed4040e5e.webp?width=670&height=670")
        
        await channel.send(embed=em)
        
        
    except:
        channel = guild.text_channels[0]
        em = discord.Embed(title = "Thanks for adding AutoBot#0521", description = "You can also add my friend **Terra#0969**, it plays 24*7 music(Youtube|Spotify|Soundcloud) [here](https://discord.com/oauth2/authorize?client_id=866674108489269288&permissions=2205281600&scope=bot%20identify%20guilds%20applications.commands&redirect_url=https://divyamsamarwal.wixsite.com/autobot/api/callback&response_type=code)", colour=discord.Color.random(), timestamp=datetime.utcnow())
        em.add_field(name="Config", value="My default prefix is **&** or **when_mentioned** <@!858965828716331019> \n You can type **&help** and get all the useful commands. \n Please make sure I have **Administrator** permissions so that every command can use be used without a problem.", inline=False)
        em.set_thumbnail(url="https://images-ext-1.discordapp.net/external/2PV16r98prv5VZyrJ8WL0usihP-cVCnw4FXAUbhtEwU/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/858965828716331019/9d6df6a23acdf3b54f96168ed4040e5e.webp?width=670&height=670")
        
        await channel.send(embed=em)

client.lavalink_nodes = [
    {"host": "host", "port": 1000, "password": "password"},
    # Can have multiple nodes here
]

client.spotify_credentials = {
    'client_id': '', 
    'client_secret': ''}




#ping
@slash.slash(name="Ping", description="Shows the latency of the bot")
async def pong(ctx):
    embed = discord.Embed(title="Pong!",
                          description=f'{round(client.latency *1000)}ms',
                          color=discord.Color.random(),
                          timestamp=datetime.utcnow())

    await ctx.send(embed=embed)



#Stats
@slash.slash(name="Stats", description="Shows stats of the bot")
async def stats(ctx):
    embed = discord.Embed(title="AutoBot Stats",
                          description="",
                          color=discord.Color.random(),
                          timestamp=datetime.utcnow())
    embed.add_field(name="Server Count",
                    value=len(client.guilds),
                    inline=False)
    embed.add_field(name="Average Latency",
                    value=round(client.latency * 1000),
                    inline=False)

    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/avatars/858965828716331019/95b08eab5679795f0dd29ab9eb3c3784.webp?size=1024'
    )

    await ctx.send(embed=embed)




#eightball


@slash.slash(name="8ball", description="Ask your questions and  get a reply")
async def Eightball(ctx, *, ques):
    responses = [
        "As I see it, yes.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.",
        "Don’t count on it.", "It is certain.", "It is decidedly so.",
        "Most likely.", "My reply is no.", "My sources say no.",
        "Outlook not so good.", "Outlook good.", "Reply hazy, try again.",
        "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.",
        "Yes – definitely.", "You may rely on it.", "*hmm*"
    ]
    embed = discord.Embed(title=" 🎱8ball ",
                          description="Questions and Answers",
                          color=discord.Color.random())
    embed.add_field(name="Question", value=f'{ques}', inline=False)
    embed.add_field(name="Answer",
                    value=f'{random.choice(responses)}',
                    inline=False)

    await ctx.send(embed=embed)


afkdict = {}


@client.command(
    name="afk",
    brief="Away From Keyboard",
    description=
    "I'll give you the afk status and if someone pings you before you come back, I'll tell "
    "them that you are not available. You can add your own afk message!")
async def afk(ctx,*, message="They didn't leave a message!"):
    global afkdict

    if ctx.message.author in afkdict:
        afkdict.pop(ctx.message.author)

        await ctx.send('Welcome back!🥱  You are no longer afk.')

    else:
        afkdict[ctx.message.author] = message
        await ctx.send("You are now afk😴!")


@client.event
async def on_message(message):
    global afkdict

    for member in message.mentions:
        if member != message.author:
            if member in afkdict:
                afkmsg = afkdict[member]
                await message.channel.send(
                    f"Oh noes! {member} is afk💤. {afkmsg}")

    await client.process_commands(message)

#math
 

@slash.slash(name="math",description="helps you in solving problems")
async def math(ctx, *, expression:str):
    calculation = eval(expression)
    embed=discord.Embed(title="Math",description='Math: {}\nAnswer: {}'.format(expression, calculation),color=discord.Colour.random(), timestamp=datetime.utcnow())
    await ctx.send(embed=embed)


datetime.utcnow()


@client.command()
@commands.bot_has_permissions(attach_files=True, embed_links=True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=discord.Colour.random(), timestamp=datetime.utcnow())
    embed.set_footer(
        text=
        "If you have any questions, suggestions or bug reports, please join our support Discord Server: Link in help command.",
        icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(
            name='Warning',
            value='Please specify what do you want me to remind you about.'
        )  # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(
            name='Warning',
            value=
            'Please specify a proper duration, send `help reminder` for more information.'
        )
    elif seconds < 180:
        embed.add_field(
            name='Warning',
            value=
            'You have specified a too short duration!\nMinimum duration is 3 minutes.'
        )
    elif seconds > 7776000:
        embed.add_field(
            name='Warning',
            value=
            'You have specified a too long duration!\nMaximum duration is 90 days.'
        )
    else:
        embed=discord.Embed(title="Reminder ⏲️",description=f"I'll will remind you in `{counter}` about **{reminder}**",color=discord.Colour.random() ,timestamp=datetime.utcnow())
        await ctx.send(embed=embed)
        await asyncio.sleep(seconds)
        await ctx.reply(
            f"{ctx.author.mention},`{counter} ago` You asked me to remind you about **{reminder}**"
        )
        return
    await ctx.send(embed=embed)

#slash

@slash.slash(name="Reminder",description="Reminds you after a specific time")
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    
    embed = discord.Embed(color=discord.Colour.random(), timestamp=datetime.utcnow())
    embed.set_footer(
        text=
        "If you have any questions, suggestions or bug reports, please join our support Discord Server: Link in help command.",
        icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(
            name='Warning',
            value='Please specify what do you want me to remind you about.'
        )  # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(
            name='Warning',
            value=
            'Please specify a proper duration, send `help reminder` for more information.'
        )
    elif seconds < 180:
        embed.add_field(
            name='Warning',
            value=
            'You have specified a too short duration!\nMinimum duration is 3 minutes.'
        )
    elif seconds > 7776000:
        embed.add_field(
            name='Warning',
            value=
            'You have specified a too long duration!\nMaximum duration is 90 days.'
        )
    else:
        embed=discord.Embed(title="Reminder ⏲️",description=f"I'll will remind you in `{counter}` about **{reminder}**",color=discord.Colour.random() ,timestamp=datetime.utcnow())
        await ctx.send(embed=embed)
        await asyncio.sleep(seconds)
        await ctx.reply(
            f"{ctx.author.mention},`{counter} ago` You asked me to remind you about **{reminder}**"
        )
        return
    await ctx.send(embed=embed)

#avatar
#serverinfo
@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)


    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
   

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=name,
                          description=f"ID :{id}",
                          color=discord.Color.random(),
                          timestamp=datetime.utcnow())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Created at",value=ctx.guild.created_at.strftime("%a , %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Members", value=memberCount, inline=True)
    embed.add_field(name="Categories", value=len(ctx.guild.categories), inline=True)
    embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels), inline=True)
    embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels), inline=True)
    embed.add_field(name="Roles",value=len(ctx.guild.roles),inline=True)
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)

    await ctx.send(embed=embed)


@slash.slash(name="Avatar", description="Shows avatar of the user")
async def avatar(ctx, * , user: discord.Member=None):
        if user is None:
            user = ctx.message.author
        embed = discord.Embed( title="This avatar seems unsual✨...",
            color=discord.Colour.random() ,timestamp=datetime.utcnow()
        )
        
        embed.add_field(name="Avatar Formats",value=f" **[Png Link]({user.avatar_url_as(format='png')})** | **[Jpg Link]({user.avatar_url_as(format='jpg')})** | **[Webp Link]({user.avatar_url_as(format='webp')})**" , inline=False)
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)    


@client.command()
async def avatar(ctx, * , user: discord.Member=None):
        if user is None:
            user = ctx.message.author
        embed = discord.Embed( title="This avatar seems unsual✨...",
            color=discord.Colour.random() ,timestamp=datetime.utcnow()
        )
        
        embed.add_field(name="Avatar Formats",value=f" **[Png Link]({user.avatar_url_as(format='png')})** | **[Jpg Link]({user.avatar_url_as(format='jpg')})** | **[Webp Link]({user.avatar_url_as(format='webp')})**" , inline=False)
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
        await ctx.send(embed=embed)    


#translator
@slash.slash(name="translate",
             description="Translates from inputed language to which you want.."
             )
async def trans(ctx, lang, *, thing):
    embed = discord.Embed(
        title="Translator🔎",
        description="Translates from inputed language to which you want..",
        color=discord.Color.random(),
        timestamp=datetime.utcnow())
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    embed.add_field(name="Inputed text", value=thing, inline=False)
    embed.add_field(name="Translated text",
                    value=translation.text,
                    inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=["translate","tl"])
async def trans(ctx, lang, *, thing):
    embed = discord.Embed(
        title="Translator🔎",
        description="Translates from inputed language to which you want..",
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
async def trans_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(
            title="API Error",
            description=
            "API => `googletrans==3.1.0a0` invoked so many errors that bot owner got tired while solving and broke the hosting server caused so much damage.\n Help us in recovering damage.\n https://www.patreon.com/AutoBot0521",
            colour=discord.Colour.random(),
            timestamp=datetime.utcnow())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/906314638428348528.gif?size=56&quality=lossless")    
        await ctx.send(embed=embed)

#pokemon

URL_API = 'https://pokeapi.co/api/v2/pokemon/'

#pokemon
@client.command()
async def pokemon(ctx, *, args):
  
    pokeName = args.lower()
    try:
        r = requests.get(f'{URL_API}{pokeName}')
        packages_json = r.json()
        packages_json.keys()

        embed = discord.Embed(title="Pokemon", color=discord.Color.random())
        embed.add_field(name="Name", value=packages_json['name'], inline=True)
        embed.add_field(name="Pokedex Order", value=packages_json['order'], inline=False)

        embed.set_thumbnail(url= f'https://play.pokemonshowdown.com/sprites/ani/{pokeName}.gif')     
        embed.add_field(name="Weight (kg)", value=packages_json['weight']/10, inline=False)
        embed.add_field(name="Height (m)", value=packages_json['height']/10, inline=False)
   
        embed.add_field(name="Base XP", value=packages_json['base_experience'], inline=False)
        for type in packages_json['types']: #FOR TO GET A TYPE OF A POKEMON
            embed.add_field(name="Types", value= type['type']['name'], inline=False)
        embed.set_footer(text=f"Requested by {ctx.author} , v1.0.2", icon_url=ctx.author.avatar_url )
        await ctx.send(embed=embed)
    except:
        await ctx.send("Pokemon not found!")

#pokemon
@slash.slash(name="pokemon",description="Shows about of pokemon.")
async def pokemon(ctx, *, args):

    pokeName = args.lower()
    try:
        r = requests.get(f'{URL_API}{pokeName}')
        packages_json = r.json()
        packages_json.keys()

        embed = discord.Embed(title="Pokemon", color=discord.Color.random())
        embed.add_field(name="Name", value=packages_json['name'], inline=True)
        embed.add_field(name="Pokedex Order", value=packages_json['order'], inline=False)

        embed.set_thumbnail(url= f'https://play.pokemonshowdown.com/sprites/ani/{pokeName}.gif')     
        embed.add_field(name="Weight (kg)", value=packages_json['weight']/10, inline=False)
        embed.add_field(name="Height (m)", value=packages_json['height']/10, inline=False)

        embed.add_field(name="Base XP", value=packages_json['base_experience'], inline=False)
        for type in packages_json['types']: #FOR TO GET A TYPE OF A POKEMON
            embed.add_field(name="Types", value= type['type']['name'], inline=False)
        embed.set_footer(text=f"Requested by {ctx.author} , v1.0.2", icon_url=ctx.author.avatar_url )
        await ctx.send(embed=embed)
    except:
        await ctx.send("Pokemon not found!")



#meme
@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="",
                          description="",
                          color=discord.Color.random(),
                          timestamp=datetime.utcnow())

    async with aiohttp.ClientSession() as cs:
        async with cs.get(
                'https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()

            embed.set_image(url=res['data']['children'][random.randint(0, 25)]
                            ['data']['url'])
            await ctx.send(embed=embed)


@slash.slash(name="dog", description="Generates random dog images!!")
async def dog(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog')
        dogjson = await request.json()
        # This time we'll get the fact request as well!
        request2 = await session.get('https://some-random-api.ml/facts/dog')
        factjson = await request2.json()

    embed = discord.Embed(title="Bow Bow!🐕", color=discord.Color.random())
    embed.set_image(url=dogjson['link'])
    embed.set_footer(text=factjson['fact'])
    await ctx.send(embed=embed)


@slash.slash(name="cat", description="Generates random cat images!!")
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(title='Kitty Cat 🐈',
                          description='Cats :star_struck:',
                          color=discord.Color.random())
    embed.set_image(url=data['file'])
    embed.set_footer(text="")
    await ctx.send(embed=embed)


#userinfo


@client.command(aliases=["ui"])
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=discord.Color.random(),
                          timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:-", value=member.id, inline=False)
    embed.add_field(name="Guild Name:-",
                    value=member.display_name,
                    inline=False)

    embed.add_field(
        name="Created At:-",
        value=member.created_at.strftime("%a , %#d %B %Y, %I:%M %p UTC"),
        inline=False)
    embed.add_field(
        name="Joined At:-",
        value=member.joined_at.strftime("%a , %#d %B %Y, %I:%M %p  UTC"),
        inline=False)

    embed.add_field(name=f"Roles:- ({len(roles)})",
                    value="".join([role.mention for role in roles]),
                    inline=False)
    embed.add_field(name="Top Role:-",
                    value=member.top_role.mention,
                    inline=False)
    embed.add_field(name="Bot?", value=member.bot, inline=False)

    await ctx.send(embed=embed)

#slash
@slash.slash(name="userinfo",description="shows the description about a specific user")
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=discord.Color.random(),
                          timestamp=datetime.utcnow())

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:-", value=member.id, inline=False)
    embed.add_field(name="Guild Name:-",
                    value=member.display_name,
                    inline=False)

    embed.add_field(
        name="Created At:-",
        value=member.created_at.strftime("%a , %#d %B %Y, %I:%M %p UTC"),
        inline=False)
    embed.add_field(
        name="Joined At:-",
        value=member.joined_at.strftime("%a , %#d %B %Y, %I:%M %p  UTC"),
        inline=False)

    embed.add_field(name=f"Roles:- ({len(roles)})",
                    value="".join([role.mention for role in roles]),
                    inline=False)
    embed.add_field(name="Top Role:-",
                    value=member.top_role.mention,
                    inline=False)
    embed.add_field(name="Bot?", value=member.bot, inline=False)

    await ctx.send(embed=embed)
#   ----------------AKINATOR


def w(name, desc, picture):
    embed_win = discord.Embed(title=f"It's {name} ({desc})! Was I correct?",
                              colour=discord.Color.random())
    embed_win.set_image(url=picture)
    return embed_win


aki = Akinator()
emojis_c = ['✅', '❌', '🤷', '👍', '👎', '⏮', '🛑']
emojis_w = ['✅', '❌']


@client.command(name='guess', aliases=["aki", "akinator"])
@commands.max_concurrency(1, per=BucketType.default, wait=False)
async def guess(ctx, *, extra):

    desc_loss = ''
    d_loss = ''

    def check_c(reaction, user):
        return user == ctx.author and str(
            reaction.emoji) in emojis_c and reaction.message.content == q

    def check_w(reaction, user):
        return user == ctx.author and str(reaction.emoji) in emojis_w

    async with ctx.typing():
        if extra == 'people':
            q = await aki.start_game(child_mode=True)
        elif extra == 'objects' or extra == 'animals':
            q = await aki.start_game(language=f'en_{extra}', child_mode=True)
        else:
            title_error_three = 'This game mode does not exist'
            desc_error_three = 'Use **.help** to see a list of all the game modes available'
            embed_var_three = discord.Embed(title=title_error_three,
                                            description=desc_error_three,
                                            colour=discord.Color.random())
            await ctx.reply(embed=embed_var_three)
            return

        embed_question = discord.Embed(
            title=
            'Tip : Wait until all emojis finish being added before reacting'
            ' or you will have to unreact and react again',
            colour=discord.Color.random())
        await ctx.reply(embed=embed_question)

    while aki.progression <= 85:
        message = await ctx.reply(q)

        for m in emojis_c:
            await message.add_reaction(m)

        try:
            symbol, username = await client.wait_for('reaction_add',
                                                     timeout=45.0,
                                                     check=check_c)
        except asyncio.TimeoutError:
            embed_game_ended = discord.Embed(
                title='You took too long,the game has ended',
                colour=discord.Color.random())
            await ctx.reply(embed=embed_game_ended)
            return

        if str(symbol) == emojis_c[0]:
            a = 'y'
        elif str(symbol) == emojis_c[1]:
            a = 'n'
        elif str(symbol) == emojis_c[2]:
            a = 'idk'
        elif str(symbol) == emojis_c[3]:
            a = 'p'
        elif str(symbol) == emojis_c[4]:
            a = 'pn'
        elif str(symbol) == emojis_c[5]:
            a = 'b'
        elif str(symbol) == emojis_c[6]:
            embed_game_end = discord.Embed(
                title='I ended the game because you asked me to do it',
                colour=discord.Color.random())
            await ctx.reply(embed=embed_game_end)
            return

        if a == "b":
            try:
                q = await aki.back()
            except akinator.CantGoBackAnyFurther:
                pass
        else:
            q = await aki.answer(a)

    await aki.win()

    wm = await ctx.reply(
        embed=w(aki.first_guess['name'], aki.first_guess['description'],
                aki.first_guess['absolute_picture_path']))

    for e in emojis_w:
        await wm.add_reaction(e)

    try:
        s, u = await client.wait_for('reaction_add',
                                     timeout=30.0,
                                     check=check_w)
    except asyncio.TimeoutError:
        for times in aki.guesses:
            d_loss = d_loss + times['name'] + '\n'
        t_loss = 'Here is a list of all the people I had in mind :'
        embed_loss = discord.Embed(title=t_loss,
                                   description=d_loss,
                                   colour=discord.Color.random())
        await ctx.reply(embed=embed_loss)
        return

    if str(s) == emojis_w[0]:
        embed_win = discord.Embed(title='Great, guessed right one more time!',
                                  colour=discord.Color.random())
        await ctx.reply(embed=embed_win)
    elif str(s) == emojis_w[1]:
        for times in aki.guesses:
            desc_loss = desc_loss + times['name'] + '\n'
        title_loss = 'No problem, I will win next time! But here is a list of all the people I had in mind :'
        embed_loss = discord.Embed(title=title_loss,
                                   description=desc_loss,
                                   colour=discord.Color.random())
        await ctx.reply(embed=embed_loss)


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@client.command(aliases=["gw"])
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx):
    await ctx.send(
        "Lets start with this giveaway! Answer this question within 15 seconds ⏳"
    )

    questions = [
        "Which channel should it be hosted in?",
        "what should be the duration of the Giveaway? (s|m|h|d)⏲️",
        "What should be the prize of the Giveaway?🎁"
    ]
    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(
                'You did not answer in time, Please be quicker next time! ⌛')
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(
            f'You did not mentioned a channel properly. Do it like this {ctx.channel.mention} next time.'
        )
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(
            f"You did not mentioned the time with a proper unit. Use (s|m|h|d) next time"
        )
        return
    elif time == -2:
        await ctx.send(
            f"The time must be an integer. Please enter an integer next time")
        return

    prize = answers[2]
    await ctx.send(
        f'🎉 The Giveaway sucessfully hosted in {channel.mention} and will last for {answers[1]}!'
    )

    embed = discord.Embed(title="Giveaway!",
                          description=f"**{prize}**",
                          color=discord.Color.random(),
                          timestamp=datetime.utcnow())

    embed.add_field(name='Hosted by :', value=ctx.author.mention)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/865177734510411816/912559896044658718/unknown-modified.png"
    )

    embed.set_footer(text=f'Ends in {answers[1]}')

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction('<a:giveaway:940195992349863976>')

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won **{prize}**")


@client.command()
@commands.has_permissions(administrator=True)
async def reroll(ctx, channel: discord.TextChannel, id_: int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send(
            "The message id was entered incorrectly, Please put the id of giveaway message"
        )
        return
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)

    await channel.send(f'Congratulations! The new winner is {winner.mention}!')


#lock
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    em = discord.Embed(
        title="LOCKDOWN🔒",
        description="**To lock the channel**\n For eg.`&lock #channelname`",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())
    em.add_field(name="Channel Succesfully locked ✅",
                 value=f'By:- {ctx.author.mention}')
    em.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/905072151680405544/916228759470891008/unknown.png"
    )
    await ctx.send(embed=em)
#slash
@slash.slash(name="lock",description="Locks a specific channel.")
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    em = discord.Embed(
        title="LOCKDOWN🔒",
        description="**To lock the channel**\n For eg.`&lock #channelname`",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())
    em.add_field(name="Channel Succesfully locked ✅",
                 value=f'By:- {ctx.author.mention}')
    em.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/905072151680405544/916228759470891008/unknown.png"
    )
    await ctx.send(embed=em)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    em = discord.Embed(
        title="UNLOCKED🔓",
        description="**To unlock the channel**\n For eg.`&unlock #channelname`",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())
    em.add_field(name="Channel Succesfully unlocked ✅",
                 value=f'By:- {ctx.author.mention}')
    em.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/895281704443465768/924537916938653706/unknown.png"
    )
    await ctx.send(embed=em)

#unlock 
@slash.slash(name="unlock",description="Unlocks a locked channel")
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    em = discord.Embed(
        title="UNLOCKED🔓",
        description="**To unlock the channel**\n For eg.`&unlock #channelname`",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())
    em.add_field(name="Channel Succesfully unlocked ✅",
                 value=f'By:- {ctx.author.mention}')
    em.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/895281704443465768/924537916938653706/unknown.png"
    )
    await ctx.send(embed=em)
#steal
@client.command(aliases=['emojisteal', 'addemoji', 'steal'])

async def stealemoji(ctx: commands.Context, emoji: Union[discord.Emoji, discord.PartialEmoji], *, name: str):
       
        try:
            emoji_bytes = await emoji.read()
            emoji_create = await ctx.guild.create_custom_emoji(image=emoji_bytes, name=name)
            await ctx.send(embed=discord.Embed(description=f"**<:tick:897382645321850920> Successfully created emoji - {emoji_create} with name: `{name}`**", color=discord.Color.green()))
            
        except Exception as e:
            error = str(e).capitalize()
            return await ctx.send(embed=discord.Embed(description=f"**<:error:897382665781669908> An error occurred while creating the emoji\n`{error}`**", color=discord.Color.red()))
#weather
# Api key from openweathermag.org

api_key = ""
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
      async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
          
            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=discord.Color.random(),
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)
    else:
        await channel.send("City not found.") 

#slash
@slash.slash(name="weather",description="shows the current weather if specified location")
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    
    if x["cod"] != "404":

            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=discord.Color.random(),
                              timestamp=datetime.utcnow())
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
    else:
        await ctx.send("City not found.") 


#role
@client.command()
@commands.has_permissions(administrator=True) #permissions
async def role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position:
    embed=discord.Embed(title="Hierarchy Error <a:wrong:940200609326444594>",description="That role is above your top role!",colour=discord.Colour.random(),timestamp=datetime.utcnow())  
    return await ctx.send(embed=embed) 
  if role in user.roles:
      await user.remove_roles(role) 
      embed=discord.Embed(title="Role Removed <a:tick:940195528103325726>",description=f"Removed {role} from {user.mention}",colour=discord.Colour.random(),timestamp=datetime.utcnow())
      await ctx.send(embed=embed)
  else:
      await user.add_roles(role)
      embed=discord.Embed(title="Role Added <a:tick:940195528103325726>",description=f"Added {role} to {user.mention}",colour=discord.Colour.random(),timestamp=datetime.utcnow())
      await ctx.send(embed=embed)

@slash.slash(name="role",description="add/remove a role from a user")
@commands.has_permissions(administrator=True) #permissions
async def role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position:
    embed=discord.Embed(title="Hierarchy Error <a:wrong:940200609326444594>",description="That role is above your top role!",colour=discord.Colour.random(),timestamp=datetime.utcnow())  
    return await ctx.send(embed=embed) 
  if role in user.roles:
      await user.remove_roles(role) 
      embed=discord.Embed(title="Role Removed <a:tick:940195528103325726>",description=f"Removed {role} from {user.mention}",colour=discord.Colour.random(),timestamp=datetime.utcnow())
      await ctx.send(embed=embed)
  else:
      await user.add_roles(role)
      embed=discord.Embed(title="Role Added <a:tick:940195528103325726>",description=f"Added {role} to {user.mention}",colour=discord.Colour.random(),timestamp=datetime.utcnow()) 
      await ctx.send(embed=embed)


@slash.slash(name="Purge", description="Clean unwanted messages or spam(s)")
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    embed = discord.Embed(
        title="Messages Purged✅",
        description=f' {limit} message(s) cleared by  {ctx.author.mention}',
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command(aliases=['purge'])
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    embed = discord.Embed(
        title="Messages Purged✅",
        description=f' {limit} message(s) cleared by  {ctx.author.mention}',
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())
    await ctx.send(embed=embed)
    await ctx.message.delete()


@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Permissions Error",
            description=
            "You do not have permission to use the `purge` command. Missing : `Administrator`",
            colour=discord.Colour.random(),
            timestamp=datetime.utcnow())
        await ctx.send(embed=embed)
#server


#info
@client.command()
async def info(ctx):

    em = discord.Embed(title = "Autobot", description = "You can add me to your server by clicking this link [here](https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=8&scope=bot%20applications.commands)", colour=discord.Color.random(), timestamp=datetime.utcnow())
    em.add_field(name="Developers", value="<@!780721106838618112> & <@!466569674335846400>" , inline=False)
    em.add_field(name="Stats",value=f'Ping :- {round(client.latency *1000)}ms \nGuilds :- {len(client.guilds)} \nUsers :- {(len(client.users))} ', inline=False)
    em.add_field(name="Github",value="[Code can be found here](https://github.com/DivyamSamarwal/Autobot)", inline=False)
    em.add_field(name="Time",value="Server location 🔆 -> California, United States of America [PST](https://time.is/PT)")
    em.add_field(name="About Developer",value="・he/him, kinda cool!! \n ・founder of Autobot/ [Infinite Domain ltd.](https://github.com/Infinite-Domain-Ltd) \n ・Hobbies :- cycling, watching anime & music. \n ・He deals 1 DPS but there is 1000% chance of crit rate. " ,  inline=False)
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/858965828716331019/9d6df6a23acdf3b54f96168ed4040e5e.webp?size=1024")
    em.set_footer(text=f"Requested by {ctx.author} , v1.0.2", icon_url=ctx.author.avatar_url  )
    await ctx.send(embed=em)

#slash
@slash.slash(name="info",description="shows the bot info")
async def info(ctx):

    em = discord.Embed(title = "Autobot", description = "You can add me to your server by clicking this link [here](https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=8&scope=bot%20applications.commands)", colour=discord.Color.random(), timestamp=datetime.utcnow())
    em.add_field(name="Developers", value="<@!780721106838618112> & <@!466569674335846400>" , inline=False)
    em.add_field(name="Stats",value=f'Ping :- {round(client.latency *1000)}ms \nGuilds :- {len(client.guilds)} \nUsers :- {(len(client.users))} ', inline=False)
    em.add_field(name="Github",value="[Code can be found here](https://github.com/DivyamSamarwal/Autobot)", inline=False)
    em.add_field(name="Time",value="Server location 🔆 -> California, United States of America [PST](https://time.is/PT)")
    em.add_field(name="About Developer",value="・he/him, kinda cool!! \n ・founder of Autobot/ [Infinite Domain ltd.](https://github.com/Infinite-Domain-Ltd) \n ・Hobbies :- cycling, watching anime & music. \n ・He deals 1 DPS but there is 1000% chance of crit rate. " ,  inline=False)
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/858965828716331019/9d6df6a23acdf3b54f96168ed4040e5e.webp?size=1024")
    em.set_footer(text=f"Requested by {ctx.author} , v1.0.2", icon_url=ctx.author.avatar_url  )
    await ctx.send(embed=em)

@client.command()
@commands.has_permissions(administrator=True)
async def lockdown(ctx, channel : discord.TextChannel=None,setting=None):
    if setting=='--server':
        for channel in ctx.guild.channels:
            await channel.set_permissions(ctx.guild.default_role, reason=f'{ctx.author.name} locked {channel.name} with --server',send_messages=False)
            embed=discord.Embed(
                timestamp=ctx.message.created_at, 
                title = "LOCKED THE SERVER 🔒",
                description=f"successfully locked the whole server by {ctx.author.mention}",
                color=ctx.author.color, 
               )
        await ctx.send(embed=embed)
    if channel is None:
        channel = ctx.message.channel
        await channel.set_permissions(ctx.guild.default_role, reason=f'{ctx.author.name} locked {channel.name}',send_messages=False)
        embed=discord.Embed(
            timestamp=ctx.message.created_at, 
                title = "LOCKDOWN 🔒",
                description=f"successfully locked the channel {ctx.author.mention}",
                color=ctx.author.color, 
               )
        await ctx.send(embed=embed)

#nickname
@client.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(title="Nickname Succesfully changed <a:tick:940195528103325726>",description=f'Nickname was changed for {member.mention}',timestamp=datetime.utcnow(), color=discord.Colour.random())
    await ctx.send(embed=embed)

#slash
@slash.slash(name="nick",description="changes the nickname of given user")
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(title="Nickname Succesfully changed <a:tick:940195528103325726>",description=f'Nickname was changed for {member.mention}',timestamp=datetime.utcnow(), color=discord.Colour.random())
    await ctx.send(embed=embed)
#anime slash
@slash.slash(name="waifu",description="shows waifu")
async def waifu(ctx,* , reason=None):
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

@slash.slash(name="kiss",description="kiss someone")

async def kiss_(ctx: commands.Context, user: discord.Member):
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

@slash.slash(name="cry",description="cry for someting")
async def cry_(ctx: commands.Context, * , reason=None):
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

@slash.slash(name="cuddle",description="cuddle someone")
async def cuddle_(ctx: commands.Context, user: discord.Member):
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

@slash.slash(name="bully",description="bully someone")

async def bully_(ctx: commands.Context, user: discord.Member):
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

@slash.slash(name="wink",description="hehe")

async def wink_(ctx: commands.Context):
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

@slash.slash(name="slap",description="slap someone")
async def slap_(ctx: commands.Context, user: discord.Member):
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

@slash.slash(name="hug",description="hug someone")
   
async def hug_(ctx: commands.Context, user: discord.Member):
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

@slash.slash(name="pat",description="pat someone")
 
async def pat_(ctx: commands.Context, user: discord.Member):
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

#slash slowmode
@slash.slash(name="slowmode",description="set customized slowmode")
async def slowmode(ctx,time:int):
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

##Genshin
@client.group(invoke_without_command=True,
              aliases=["gs"])
async def genshin(ctx):
    em = discord.Embed(
        title="Genshin Impact",
        description=
        "There are currently **42 Genshin Impact characters** available,so there's no shortage of candidates for your dream team.",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())

    em.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/913285590580076625/913285606119968778/2560px-Genshin_Impact_logo.png"
    )
    em.set_image(
        url=
        "https://media.discordapp.net/attachments/913285590580076625/913300408510873710/download.gif"
    )
    em.add_field(name="Elementals",
                 value="`Pyro|Hydro|Anemo|Dendro|Electro|Cryo|Geo`",
                 inline=False)
    em.add_field(name="Characters Details",
                 value="command`<character_name>`",
                 inline=False)
    em.set_footer(text="©️miHoYo Co., Ltd.")
    await ctx.send(embed=em)


@genshin.command(aliases=["aether", "traveler"])
async def lumine(ctx):
    em = discord.Embed(title="Traveler",
                       description="Lumine/Aether (Anemo|Geo|Electro)")
    em.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/895281704443465768/913376119808479253/t0cg7qqhz4angz8m_1602753471.png"
    )

    await ctx.send(embed=em)


@genshin.command(aliases=["tier list"])
async def tierlist(ctx):
    em = discord.Embed(title="Genshin  Impact",
                       description="Charactes Tier List",
                       colour=discord.Colour.random(),
                       timestamp=datetime.utcnow())
    em.add_field(
        name="__SS Tier__",
        value=
        "`Shenhe | Itto | Raiden | Ayaka | Zhongli | Ganyu | Kazuha | Venti | Xiao | Bennett | Hu Tao | Xingqiu`",
        inline=False)
    em.add_field(
        name="__S Tier__",
        value=
        "`Kokomi | Yoimiya | Jean | Diona | Klee | Eula | Mona | Sucrose | Chongyun | Albedo | Diluc | Targitalia | Xiangling`",
        inline=False)
    em.add_field(
        name="__A Tier__",
        value=
        "`Yun Jin | Gorou | Thoma | Aloy | Kujou | Sayu | Qiqi | Beidou | Keqing | Nigguang | Fischl`",
        inline=False)
    em.add_field(
        name="__B Tier__",
        value=
        "`Kaeya | Razor | Yanfei | Barbara | Noelle | Rosaria | Traveler(Geo/Electro)`",
        inline=False)
    em.add_field(name="__C Tier__",
                 value="`Lisa | Amber | Xinyan | Traveler(Anemo)`",
                 inline=False)

    await ctx.send(embed=em)


#help
@slash.slash(name="help", description="Get to know about my commands")
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description=
        "Use **&help** `<command>` for more information about the command.",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())

    em.set_image(
        url=
        "https://cdn.discordapp.com/attachments/858354774810689557/928949260161019944/standard_5.gif")

    em.add_field(name="Fun <a:fun:940198380309737472>",
                 value="`8Ball,Guess,Imagine,Giveaway,dog,cat,meme`",
                 inline=False)
    em.add_field(name="Info <:Inform:940198203435929710>",
                 value="`Avatar,Serverinfo,info,Stats,Userinfo,poll,tally,nick`",
                 inline=False)
    em.add_field(name="Special <a:Special:940197538810720266>",
                 value="`Reminder,role,Translate,afk,lock,unlock,slowmode,weather,math`",
                 inline=False)
    em.add_field(name="Anime <:keqing:939052537699512340>",
                 value="`anime,character,animenews,waifu,kiss,cry,cuddle,bully,wink,slap,hug,pat`",
                 inline=False)
    
    em.add_field(
        name="Music <a:music:940196835052646411>",
        value=
        "`connect,disconnect,play,skip,pause,resume,seek <seconds>,volume <vol>,loop,nowplaying,queue.`",
        inline=False
    )
    em.add_field(
        name="Other 📜",
        value=
        "[Invite](https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=8&scope=bot%20applications.commands), [AutoBot Help ❓](https://discord.gg/nUFxsaGMQq) , [Patreon 💖](https://www.patreon.com/AutoBot0521) , [Vote](https://top.gg/bot/858965828716331019) ,[Terra Music Bot](https://discord.com/oauth2/authorize?client_id=866674108489269288&permissions=2205281600&scope=bot%20identify%20guilds%20applications.commands)",
        inline=False    
    )

    em.set_footer(text=f"Requested by {ctx.author}",
                    icon_url=ctx.author.avatar_url)

    await ctx.send(embed=em)


client.remove_command("help")


@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description=
        "Use **&help** `<command>` for more information about the command",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())

    em.set_image(
        url=
        "https://cdn.discordapp.com/attachments/858354774810689557/928949260161019944/standard_5.gif"
    )

    em.add_field(name="Fun <a:fun:940198380309737472>",
                 value="`8Ball,Guess,Imagine,Giveaway,dog,cat,meme`",
                 inline=False)
    em.add_field(name="Info <:Inform:940198203435929710>",
                 value="`Avatar,Serverinfo,info,Stats,Userinfo,poll,tally`",
                 inline=False)
    em.add_field(name="Special <a:Special:940197538810720266>",
                 value="`Reminder,nick,Translate,afk,lock,unlock,slowmode,weather,math`",
                 inline=False)
    em.add_field(name="Anime <:keqing:939052537699512340>",
                 value="`anime,character,animenews,waifu,kiss,cry,cuddle,bully,wink,slap,hug,pat`",
                 inline=False)
    em.add_field(
        name="Music <a:music:940196835052646411>",
        value=
        "`connect,disconnect,play,skip,pause,resume,seek <seconds>,volume <vol>,loop,nowplaying,queue.`",
        inline=False
    )
    em.add_field(
        name="Other 📜",
        value=
        "[Invite](https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=8&scope=bot%20applications.commands), [AutoBot Help ❓](https://discord.gg/nUFxsaGMQq) , [Patreon 💖](https://www.patreon.com/AutoBot0521) , [Vote](https://top.gg/bot/858965828716331019) , [Terra Music Bot](https://discord.com/oauth2/authorize?client_id=866674108489269288&permissions=2205281600&scope=bot%20identify%20guilds%20applications.commands)",
        inline=False    
    )
    em.set_footer(text=f"Requested by {ctx.author}",
                    icon_url=ctx.author.avatar_url)

    await ctx.send(embed=em)

#help inbuilds


@help.command()
async def math(ctx):
    em = discord.Embed(
        title="Calculator",
        description=
        " It is something used for making mathematical calculations  ",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())
    em.add_field(name="For Addition :-",
                 value="`Number 1` + `Number 2` = **Sum** ",
                 inline=False)
    em.add_field(name="For Subtraction :-",
                 value="`Number 1` - `Number 2` = **Difference** ",
                 inline=False)
    em.add_field(name="For Multiplication :-",
                 value="`Number 1` * `Number 2` = **Product** ",
                 inline=False)
    em.add_field(name="For Division :-",
                 value="`Number 1` / `Number 2` = **Quotient** ",
                 inline=False)
    em.add_field(name="For Exponential :-",
                 value="`Number 1`^`Number 2` = **number1^number2**",
                 inline=False)
    em.add_field(
        name="For Remainder :-",
        value=
        "`Number 1` // `Number 2` = **Remainder If not fully divisible.** ",
        inline=False)
    await ctx.send(embed=em)


@help.command(aliases=["gw", "GW"])
async def giveaway(ctx):
    em = discord.Embed(title="Giveaway",
                       description="Make giveaways with this command easily",
                       colour=discord.Colour.random())
    em.add_field(name="Making a giveaway🎉",
                 value="`prefix`giveaway",
                 inline=False)
    em.add_field(
        name="Rerolling a giveaway",
        value=
        "`prefix`reroll<channelname><messageid>\n **Channelname** should be the channel where you *hosted* giveaway.\n **MessageID** should be an *integer.*",
        inline=False)
    await ctx.send(embed=em)


@help.command()
async def afk(ctx):
    em = discord.Embed(title="Commands Settings",
                       description="AFK :- Away from keys",
                       colour=discord.Colour.random())
    em.add_field(
        name="**Set an AFK status to display when you are mentioned⚙️**",
        value="<prefix>afk")
    await ctx.send(embed=em)

@help.command()
async def lockdown(ctx):
    em = discord.Embed(title="Server Lockdown",
                       description="Locks the whole server. ",
                       colour=discord.Colour.random())
    em.add_field(
        name="**Usage ⚙️**",
        value=
        ">> `&lockdown #channel_name --server`\n>> `requires admin permissions` \n>> `saves the server from the raid` \n>> `use this wisely(not for checking)` \n>> `you have to unlock each channel.`"    
    )
    await ctx.send(embed=em)


@help.command(aliases=["tl", "TL"])
async def translate(ctx):
    em = discord.Embed(title="Commands Settings",
                       description="Translates one language to other",
                       colour=discord.Colour.random())
    em.add_field(name="**Translator⚙️**",
                 value="<language you want to translate>arguments")

    await ctx.send(embed=em)


@help.command()
async def reminder(ctx):
    em = discord.Embed(title="Commands Setting",
                       description="Reminds at specific time ",
                       colour=discord.Colour.random())
    em.add_field(
        name="** Set a reminder ⚙️**",
        value=
        "`prefix command`<[amount of time in digits] seconds of s , minutes of m and hours for h , days for d>`<your message>`"
    )
    await ctx.send(embed=em)


@help.command()
async def guess(ctx):
    desc_helpme = '__**HOW TO PLAY**__\n\nUse the `<prefix>guess` command followed by the game mode you want to play. Here is ' \
       'a list of currently available game modes : **people, animals, objects**.\nFor example : `<prefix>guess people`\n\n__**GAME MODES**__\n\n' \
       '**People** : This is the game mode for guessing people (fictional or real)\n**Animals** : ' \
       'This is the game mode for guessing animals\n**Objects** : This is the game mode for guessing objects' \
       '\n\n__**MISCELLANEOUS**__\n\n**1.**Wait until all emojis are displayed before adding your reaction, or' \
       ' else it will not register it and you will have to react again once it is done displaying' \
       '\n**2.**The game ends in 45 seconds if you do not answer the question by reacting with the right' \
       ' emoji\n**3.** The bot might sometimes be slow, please be patient and wait for it to ask you the questions. If it is stuck, do not worry the game will automatically end in 30 seconds and you can start playing again\n**4.** Only one person can play at a time\n\n' \
       '__**EMOJI MEANINGS**__\n\n✅ = This emoji means "yes"\n❌ = This emoji means "no"\n🤷 = This emoji means' \
       '"I do not know"\n👍 = This emoji means "probably"\n👎 = This emoji means "probably not"\n⏮ = This ' \
       'emoji repeats the question before\n🛑 = This emoji ends the game being played'
    embed_var_helpme = discord.Embed(description=desc_helpme,
                                     colour=discord.Color.random())
    await ctx.send(embed=embed_var_helpme)

import traceback
import sys

extensions=[ 'cogs.anime', 'cogs.utility','cogs.general']

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Error Loading{extension}', file=sys.stderr)
            traceback.print_exc()




@client.command()
@is_owner()
async def check_cogs(ctx, cog_name):
    try:
        client.load_extension(f"cogs.{cog_name}")
    except commands.ExtensionAlreadyLoaded:
        message = await ctx.send('`💎` You are the `Jishaku` of this bot. \n あなたはこのボットのジシャクです。')
        await message.edit(content="<a:settings:940198899715555359>")
        await message.edit(content=f'**{cog_name}** cog is loaded <a:settings:940198899715555359>')
    except commands.ExtensionNotFound:
        await ctx.send("Cog not found")
    else:
        await ctx.send("Cog is unloaded")
        client.unload_extension(f"cogs.{cog_name}")

@check_cogs.error
async def check_cogs_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        embed = discord.Embed(
            title="Permmissions Denied <a:wrong:940200609326444594>",
            description=
            "`💠` You are not `Shogunate` of this bot.\n `💠` あなたはこのボットの幕府ではありません。 ",
            colour=discord.Colour.random(),
            timestamp=datetime.utcnow())
        await ctx.send(embed=embed)


keep_alive()

my_secret = os.environ['Token']
client.run(my_secret)

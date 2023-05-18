from asyncio.tasks import wait
from time import time
from typing import Optional
import discord
import random
from discord import colour
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

import deep_translator
from deep_translator import GoogleTranslator
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
from typing import Union
import math
from webserver import keep_alive
import sys
import traceback
import os
from aiohttp import request

from discord.ext import commands
from discord.ext.commands import BucketType
import requests
import aiohttp
import psutil

intents = discord.Intents.all()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(commands.when_mentioned_or('&'),
                      intents=intents,
                      case_insensitive=True)
client.launch_time = datetime.utcnow()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(
                                     type=discord.ActivityType.playing,
                                     name=f'@Autobot'))
    print(' Hello I am AutoBot. ')


#on_guild_join
@client.event
async def on_guild_join(guild):
    try:
        channel = guild.system_channel
        em = discord.Embed(
            title="Thanks for adding AutoBot#0521",
            description=
            "You can also add my friend **Terra#0969**, it plays 24*7 music(Youtube|Spotify|Soundcloud) [here](https://discord.com/oauth2/authorize?client_id=866674108489269288&permissions=2205281600&scope=bot%20identify%20guilds%20applications.commands&redirect_url=https://divyamsamarwal.wixsite.com/autobot/api/callback&response_type=code)",
            colour=discord.Color.random(),
            timestamp=datetime.utcnow())
        em.add_field(
            name="Config",
            value=
            "My default prefix is **&** or **when_mentioned** <@!858965828716331019> \n You can type **&help** and get all the useful commands. \n Please make sure I have **Administrator** permissions so that every command can use be used without a problem.",
            inline=False)
        em.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2PV16r98prv5VZyrJ8WL0usihP-cVCnw4FXAUbhtEwU/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/858965828716331019/9d6df6a23acdf3b54f96168ed4040e5e.webp?width=670&height=670"
        )

        await channel.send(embed=em)

    except:
        channel = guild.text_channels[0]
        em = discord.Embed(
            title="Thanks for adding AutoBot#0521",
            description=
            "You can also add my friend **Terra#0969**, it plays 24*7 music(Youtube|Spotify|Soundcloud) [here](https://discord.com/oauth2/authorize?client_id=866674108489269288&permissions=2205281600&scope=bot%20identify%20guilds%20applications.commands&redirect_url=https://divyamsamarwal.wixsite.com/autobot/api/callback&response_type=code)",
            colour=discord.Color.random(),
            timestamp=datetime.utcnow())
        em.add_field(
            name="Config",
            value=
            "My default prefix is **&** or **when_mentioned** <@!858965828716331019> \n You can type **&help** and get all the useful commands. \n Please make sure I have **Administrator** permissions so that every command can use be used without a problem.",
            inline=False)
        em.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2PV16r98prv5VZyrJ8WL0usihP-cVCnw4FXAUbhtEwU/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/858965828716331019/9d6df6a23acdf3b54f96168ed4040e5e.webp?width=670&height=670"
        )

        await channel.send(embed=em)


client.lavalink_nodes = [
    {
        "host": "losingtime.dpaste.org",
        "port": 2124,
        "password": "SleepingOnTrains"
    },
    # Can have multiple nodes here
]

client.spotify_credentials = {
    'client_id': '0a7f52a35b814c9396c42cd27c07a139',
    'client_secret': 'e9bdf41a4bf046f1b62b733e4269d69e'
}

#important
import psutil


@client.hybrid_command()
async def usage(ctx):
    bedem = discord.Embed(
        title='System Resource Usage',
        description='See CPU and memory usage of the system.')
    bedem.add_field(name='CPU Usage',
                    value=f'{psutil.cpu_percent()}%',
                    inline=False)
    bedem.add_field(name='Memory Usage',
                    value=f'{psutil.virtual_memory().percent}%',
                    inline=False)
    bedem.add_field(
        name='Available Memory',
        value=
        f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%',
        inline=False)
    await ctx.send(embed=bedem)


@client.hybrid_command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")


#ping
@client.hybrid_command()
async def ping(ctx):
    embed = discord.Embed(title="Pong!",
                          description=f'{round(client.latency *1000)}ms',
                          color=discord.Color.random(),
                          timestamp=datetime.utcnow())

    await ctx.send(embed=embed)


#Stats
@client.hybrid_command()
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


@client.hybrid_command()
async def invite(ctx):
    embed = discord.Embed(
        title="Invite",
        description=
        "[Click Here](https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=8&scope=bot%20applications.commands)",
        color=discord.Color.random(),
        timestamp=datetime.utcnow())
    await ctx.send(embed=embed)


#eightball


@client.hybrid_command()
async def eightball(ctx, *, ques):
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
async def afk(ctx, *, message="They didn't leave a message!"):
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


datetime.utcnow()


@client.hybrid_command()
@commands.bot_has_permissions(attach_files=True, embed_links=True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=discord.Colour.random(),
                          timestamp=datetime.utcnow())
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
        embed = discord.Embed(
            title="Reminder ⏲️",
            description=
            f"I'll will remind you in `{counter}` about **{reminder}**",
            color=discord.Colour.random(),
            timestamp=datetime.utcnow())
        await ctx.send(embed=embed)
        await asyncio.sleep(seconds)
        await ctx.reply(
            f"{ctx.author.mention},`{counter} ago` You asked me to remind you about **{reminder}**"
        )
        return
    await ctx.send(embed=embed)


@client.hybrid_command()
async def math(ctx, *, expression: str):
    calculation = eval(expression)
    embed = discord.Embed(title="Math",
                          description='Expression: {}\nAnswer: {}'.format(
                              expression, calculation),
                          color=discord.Colour.random(),
                          timestamp=datetime.utcnow())
    await ctx.send(embed=embed)


#translator
@client.hybrid_command()
async def translate(ctx, lang, *, thing):
    embed = discord.Embed(
        title="Translator🔎",
        description="Translates from inputed language to which you want..",
        color=discord.Color.random(),
        timestamp=datetime.utcnow())
    translation = GoogleTranslator(source='auto', target=lang).translate(thing)
    embed.add_field(name="Inputed text", value=thing, inline=False)
    embed.set_footer(text="For shortforms visit the repository in github.")
    embed.add_field(name=f"Translated text to {lang}",
                    value=translation,
                    inline=False)
    embed.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/862599394712354831/985831579500830750/translator.png"
    )
    await ctx.send(embed=embed)


#role
@client.hybrid_command()
@commands.has_permissions(administrator=True)  #permissions
async def role(ctx, user: discord.Member, *, role: discord.Role):
    if role.position > ctx.author.top_role.position:
        embed = discord.Embed(
            title="Hierarchy Error <a:wrong:940200609326444594>",
            description="That role is above your top role!",
            colour=discord.Colour.random(),
            timestamp=datetime.utcnow())
        return await ctx.send(embed=embed)
    if role in user.roles:
        await user.remove_roles(role)
        embed = discord.Embed(
            title="Role Removed <a:tick:940195528103325726>",
            description=f"Removed {role} from {user.mention}",
            colour=discord.Colour.random(),
            timestamp=datetime.utcnow())
        await ctx.send(embed=embed)
    else:
        await user.add_roles(role)
        embed = discord.Embed(title="Role Added <a:tick:940195528103325726>",
                              description=f"Added {role} to {user.mention}",
                              colour=discord.Colour.random(),
                              timestamp=datetime.utcnow())
        await ctx.send(embed=embed)


#pokemon

URL_API = 'https://pokeapi.co/api/v2/pokemon/'


@client.hybrid_command()
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(title='Kitty Cat 🐈',
                          description='Cats :star_struck:',
                          color=discord.Color.random())
    embed.set_image(url=data['file'])
    embed.set_footer(text="")
    await ctx.send(embed=embed)


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


@client.hybrid_command()
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


@client.hybrid_command()
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
@client.hybrid_command()
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


@client.hybrid_command()
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


#weather
# Api key from openweathermag.org

api_key = "6e62189453be0c6774c53f9050e4c1b7"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@client.hybrid_command()
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
            current_temperature_celsiuis = str(
                round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            embed = discord.Embed(
                title=f"Weather in {city_name}",
                color=discord.Color.random(),
                timestamp=ctx.message.created_at,
            )
            embed.add_field(name="Descripition",
                            value=f"**{weather_description}**",
                            inline=False)
            embed.add_field(name="Temperature(C)",
                            value=f"**{current_temperature_celsiuis}°C**",
                            inline=False)
            embed.add_field(name="Humidity(%)",
                            value=f"**{current_humidity}%**",
                            inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)",
                            value=f"**{current_pressure}hPa**",
                            inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)
    else:
        await channel.send("City not found.")


#------BUGS
@client.hybrid_command()
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


@client.hybrid_command()
@commands.has_permissions(administrator=True)
async def lockdown(ctx, channel: discord.TextChannel = None, setting=None):
    if setting == '--server':
        for channel in ctx.guild.channels:
            await channel.set_permissions(
                ctx.guild.default_role,
                reason=f'{ctx.author.name} locked {channel.name} with --server',
                send_messages=False)
            embed = discord.Embed(
                timestamp=ctx.message.created_at,
                title="LOCKED THE SERVER 🔒",
                description=
                f"successfully locked the whole server by {ctx.author.mention}",
                color=ctx.author.color,
            )
        await ctx.send(embed=embed)
    if channel is None:
        channel = ctx.message.channel
        await channel.set_permissions(
            ctx.guild.default_role,
            reason=f'{ctx.author.name} locked {channel.name}',
            send_messages=False)
        embed = discord.Embed(
            timestamp=ctx.message.created_at,
            title="LOCKDOWN 🔒",
            description=f"successfully locked the channel {ctx.author.mention}",
            color=ctx.author.color,
        )
        await ctx.send(embed=embed)


#nickname
@client.hybrid_command()
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    embed = discord.Embed(
        title="Nickname Succesfully changed <a:tick:940195528103325726>",
        description=f'Nickname was changed for {member.mention}',
        timestamp=datetime.utcnow(),
        color=discord.Colour.random())
    await ctx.send(embed=embed)


#slash


#anime slash
@client.hybrid_command()
async def waifu(ctx, *, reason=None):
    """Waifu"""

    url = "https://api.waifu.pics/sfw/waifu"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=
                f"<:keqing:939052537699512340> Requested by {ctx.author.name}",
                color=discord.Colour.random(),
                timestamp=datetime.utcnow())
            embed.set_image(url=data['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)


@client.hybrid_command()
@is_owner()
async def nwaifu(ctx, *, reason=None):
    """Waifu"""

    url = "https://api.waifu.pics/nsfw/waifu"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=
                f"<:keqing:939052537699512340> Requested by {ctx.author.name}",
                color=discord.Colour.random(),
                timestamp=datetime.utcnow())
            embed.set_image(url=data['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)


@client.hybrid_command()
async def kiss_(ctx: commands.Context, user: discord.Member):
    """Kiss someone"""

    url = "https://api.waifu.pics/sfw/kiss"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=f"{ctx.author.mention} kisses {user.mention}",
                color=discord.Colour.green())
            embed.set_image(url=data['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)


@client.hybrid_command()
async def cry_(ctx: commands.Context, *, reason=None):
    """Anime Cry for something"""

    url = "https://api.waifu.pics/sfw/cry"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=
                f"{ctx.author.mention} is crying for \n reason : **{reason}**",
                color=discord.Colour.green())
            embed.set_image(url=data['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)


@client.hybrid_command()
async def cuddle_(ctx: commands.Context, user: discord.Member):
    """Cuddle Someone"""

    url = "https://api.waifu.pics/sfw/cuddle"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=f"{ctx.author.mention} cuddles {user.mention}",
                color=discord.Colour.green())
            embed.set_image(url=data['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)


@client.hybrid_command()
async def bully_(ctx: commands.Context, user: discord.Member):
    """Bully Someone"""

    url = "https://api.waifu.pics/sfw/bully"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=f"{ctx.author.mention} bullies {user.mention}",
                color=discord.Colour.green())
            embed.set_image(url=data['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)


@client.hybrid_command()
async def wink_(ctx: commands.Context):
    """wink your eye"""

    url = "https://api.waifu.pics/sfw/wink"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=f"{ctx.author.mention} Your wink is unique",
                color=discord.Colour.green())
            embed.set_image(url=data['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)
            #await ctx.send(f"API ERRORS {response.status}status.")


@client.hybrid_command()
async def slap_(ctx: commands.Context, user: discord.Member):
    """Slap someone"""
    if user.bot:
        return await ctx.send(embed=discord.Embed(
            description=
            "**<a:wrong:940200609326444594> You can't slap a bot.**",
            color=discord.Colour.red()))
    if user == ctx.author:
        return await ctx.send(embed=discord.Embed(
            description=
            "**<a:wrong:940200609326444594> You can't slap yourself! Try slapping someone else.**",
            color=discord.Colour.red()))

    url = "https://neko-love.xyz/api/v1/slap"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=f"{ctx.author.mention} slaps {user.mention}",
                color=discord.Colour.green())
            embed.set_image(url=data['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)
            #await ctx.send(f"API ERRORS {response.status}status.")


@client.hybrid_command()
async def hug_(ctx: commands.Context, user: discord.Member):
    """Hug someone"""
    if user.bot:
        return await ctx.send(embed=discord.Embed(
            description="**<a:wrong:940200609326444594> You can't hug a bot.**",
            color=discord.Colour.red()))
    if user == ctx.author:
        return await ctx.send(embed=discord.Embed(
            description=
            "**<a:wrong:940200609326444594> You can't hug yourself! Try hugging someone else.**",
            color=discord.Colour.red()))

    url = "https://some-random-api.ml/animu/hug"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=f"{ctx.author.mention} hugs {user.mention}",
                color=discord.Colour.green())
            embed.set_image(url=data['link'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)
            #await ctx.send(f"API ERRORS {response.status}status.")


@client.hybrid_command()
async def pat_(ctx: commands.Context, user: discord.Member):
    """Pat someone"""
    if user.bot:
        return await ctx.send(embed=discord.Embed(
            description=
            "** <a:wrong:940200609326444594> You can't pat a bot.**",
            color=discord.Colour.red()))
    if user == ctx.author:
        return await ctx.send(embed=discord.Embed(
            description=
            "**<a:wrong:940200609326444594> You can't pat yourself! Try patting someone else.**",
            color=discord.Colour.red()))

    url = "https://some-random-api.ml/animu/pat"
    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            embed = discord.Embed(
                description=f'{ctx.author.mention} patted {user.mention}',
                color=discord.Colour.green())
            embed.set_image(url=data['link'])
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                description=f"API ERRORS {response.status}status.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)
            #await ctx.send(f"API ERRORS {response.status}status.")


#slash slowmode
@client.hybrid_command()
async def slowmode(ctx, time: int):
    if (not ctx.author.guild_permissions.manage_messages):
        embed = discord.Embed(
            title="Permission error",
            description=
            "This requires `Manage Message Permission`.You don't have that!",
            color=discord.Colour.dark_red())
        await ctx.send(embed=embed)
        return
    try:
        if time == 0:
            embed1 = discord.Embed(
                title="Slowmode succesfully off",
                description=
                "If time has been set to 0 seconds then slowmode would be off. <a:tick:940195528103325726>",
                color=discord.Colour.dark_teal())
            await ctx.send(embed=embed1)
            await ctx.channel.edit(slowmode_delay=0)
        elif time > 21600:
            emb = discord.Embed(
                title="Time Error <a:wrong:940200609326444594>",
                description="You can not set the slowmode above `6 hours`",
                color=discord.Colour.red())
            emb.add_field(
                name="Quick Conversions",
                value=
                "1 min =  60 seconds \n 2 min = 120 seconds \n 5 min = 300 seconds \n 1 hour = 3600 seconds \n 6 hours = 21600 seconds"
            )
            await ctx.send(embed=emb)
            return
        else:
            await ctx.channel.edit(slowmode_delay=time)
            em = discord.Embed(
                title="Succesfully set! <a:tick:940195528103325726>",
                description=f"Slowmode set to {time} seconds",
                color=discord.Colour.teal())
            await ctx.send(embed=em)
    except Exception:
        await print("Oops!")

# WILL FIX SOON
"""
@client.hybrid_command()
async def help(ctx):
    em = discord.Embed(
        title="HELP <:settings:984688397400551436> ",
        description=
        "Use **&help** `<command>` for more information about the command!!",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())

    em.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/862599394712354831/984689351390801940/unknown.png"
    )

    em.add_field(name="<:folder:984688392333840394> FUN",
                 value="<:pointers:984688394955284540>`8ball`\n<:pointers:984688394955284540>`guess`\n<:pointers:984688394955284540>`imagine`\n<:pointers:984688394955284540>`giveaway`\n<:pointers:984688394955284540>`dog`\n<:pointers:984688394955284540>`cat`\n<:pointers:984688394955284540>`meme`",
                 inline=True)
    em.add_field(name="<:folder:984688392333840394> INFO",
                 value="<:pointers:984688394955284540>`avatar`\n<:pointers:984688394955284540>`serverinfo`\n<:pointers:984688394955284540>`info`\n<:pointers:984688394955284540>`stats`\n<:pointers:984688394955284540>`userinfo`\n<:pointers:984688394955284540>`poll`\n<:pointers:984688394955284540>`tally`",
                 inline=True)
    em.add_field(name="<:folder:984688392333840394> SPECIAL",
                 value="<:pointers:984688394955284540>`reminder`\n<:pointers:984688394955284540>`nick`\n<:pointers:984688394955284540>`translate`\n<:pointers:984688394955284540>`afk`\n<:pointers:984688394955284540>`lock`\n<:pointers:984688394955284540>`unlock`\n<:pointers:984688394955284540>`slowmode`\n<:pointers:984688394955284540>`weather`\n<:pointers:984688394955284540>`math`",
                 inline=True)
    em.add_field(name="<:folder:984688392333840394> ANIME",
                 value="<:pointers:984688394955284540>`anime`\n<:pointers:984688394955284540>`character`\n<:pointers:984688394955284540>`animenews`\n<:pointers:984688394955284540>`waifu`\n<:pointers:984688394955284540>`kiss`\n<:pointers:984688394955284540>`cry`\n<:pointers:984688394955284540>`cuddle`\n<:pointers:984688394955284540>`bully`\n<:pointers:984688394955284540>`wink`\n<:pointers:984688394955284540>`slap`\n<:pointers:984688394955284540>`hug`\n<:pointers:984688394955284540>`pat`",
                 inline=True)
    em.add_field(
        name="<:folder:984688392333840394> LINKS",
        value=
        "<:link:984697304869113916>[Invite](https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=8&scope=bot%20applications.commands)\n<:memory:940222649517375509>[AutoBot Server](https://discord.gg/nUFxsaGMQq)\n<:patreon:984698110909501442>[Patreon](https://www.patreon.com/AutoBot0521)\n<:topgg:984698778453934150>[Vote](https://top.gg/bot/858965828716331019)\n<:Inform:940198203435929710>[Terra Music](https://discord.com/oauth2/authorize?client_id=866674108489269288&permissions=2205281600&scope=bot%20identify%20guilds%20applications.commands)",
        inline=True    
    )
    em.set_footer(text=f"Requested by {ctx.author}",
                    icon_url=ctx.author.avatar_url)

    await ctx.send(embed=em)
client.remove_command("help")

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
"""

keep_alive()

my_secret = os.environ['Token']
client.run(my_secret)

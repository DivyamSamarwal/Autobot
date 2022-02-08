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
from webserver import keep_alive

import os

import akinator
from discord.ext import commands
from akinator.async_aki import Akinator

from discord.ext.commands import BucketType
import requests
import aiohttp
intents = discord.Intents.all()

my_default_prefix = "&"


def get_prefix(client, message):  # declare lol
    with open("prefixes.json", "r") as f:  # opening the file ofc
        prefixes = json.load(f)
    try:
        prefix = prefixes[str(
            message.guild.id)]  # trying to get the prefix ( if exists )
    except KeyError:  # catching the error
        prefix = my_default_prefix  # if no prefix found, setting prefix as default prefix

    return prefix  # returning the prefix Ez


client = commands.Bot(command_prefix=get_prefix)
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "&"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)


@client.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)

    await ctx.send(f"The prefix was changed to {prefix}")


@client.event
async def on_message(message):

    mention = f'<@!{client.user.id}>'
    if message.content == mention:
        with open(
                'prefixes.json', 'r'
        ) as f:  ##we open and read the prefixes.json, assuming it's in the same file
            prefixes = json.load(f)  #load the json as prefixes
        prefix = prefixes[str(message.guild.id)]
        await message.channel.send(
            f"You called? My prefix for this server is `{prefix}`. Admins can change it by using `{prefix}changeprefix <new prefix>`"
        )
    await client.process_commands(message)


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=f'&help and Watching {len(client.guilds) } Severs'))
    print(' Hello I am AutoBot. ')
    client.load_extension('dismusic')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**Still on Cooldown**,please try again in ** {:.2f}s **'.format(
            error.retry_after)
        await ctx.send(msg)







#ping
@slash.slash(name="Ping", description="Shows the latency of the bot")
@commands.cooldown(3, 10, commands.BucketType.user)
async def pong(ctx):
    embed = discord.Embed(title="Pong!",
                          description=f'{round(client.latency *1000)}ms',
                          color=discord.Color.random(),
                          timestamp=datetime.utcnow())

    await ctx.send(embed=embed)


@client.command(aliases=['latency', 'Ping', 'PING'])
@commands.cooldown(3, 10, commands.BucketType.user)
async def ping(ctx):
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


@client.command(aliases=['8ball', '8b'])
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


@client.command(aliases=['Imagine', 'IMAGINE'])
@commands.cooldown(3, 10, commands.BucketType.user)
async def imagine(ctx):
    responses = [
        "https://media.discordapp.net/attachments/862895445381218334/871692994955329567/My_Post.png?width=1078&height=606",
        "https://media.discordapp.net/attachments/862895445381218334/871698288053723136/My_Post_1.png?width=1078&height=606",
        "https://media.discordapp.net/attachments/862895445381218334/871710199931621396/My_Post_2.png?width=1078&height=606"
    ]
    message = await ctx.send(' `Imagining...`')
    await message.edit(content=" `10% complete`")
    await message.edit(content=" `50% complete`")
    await message.edit(content=" `100% complete`")
    await message.edit(content=f' {random.choice(responses)}')


#serverinfo

@client.command(
    aliases=["hello", "HI", "Hi", "Hello", "HELLO", "こんにちは", "नमस्ते", "你好"])
async def hi(ctx):
    embed = discord.Embed(title="Hello",
                          description="I am Autobot",
                          color=discord.Color.random())
    embed.add_field(name="Wassup!", value="Nice to meet you")

    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/866949734512853012/866949844543209502/unknown.png"
    )

    await ctx.send(embed=embed)


afkdict = {}


@client.command(
    name="afk",
    brief="Away From Keyboard",
    description=
    "I'll give you the afk status and if someone pings you before you come back, I'll tell "
    "them that you are not available. You can add your own afk message!")
async def afk(ctx, message="They didn't leave a message!"):
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


@client.command(case_insensitive=True,
                aliases=["remind", "remindme", "remind_me", "Reminder"])
@commands.bot_has_permissions(attach_files=True, embed_links=True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
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
        await ctx.send(
            f"Alright, I will remind {user} about {reminder} in {counter}.")
        await asyncio.sleep(seconds)
        await ctx.reply(
            f"Hi, you asked me to remind you about {user} {reminder} {counter} ago."
        )
        return
    await ctx.send(embed=embed)


#avatar


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


@client.command(aliases=["translate", "Translate", "tl", "TL", "Tl"])
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


@client.command(aliases=["Userinfo", "ui", "UserInfo"])
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


#music

client.lava_nodes = [{
    'host': 'lava.link',
    'port': 80,
    'rest_uri': f'http://lava.link:80',
    'identifier': 'MAIN',
    'password': 'anything',
    'region': 'singapore'
}]


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


@client.command(aliases=["gw", "GW", "Giveaway"])
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

#------BUGS

    

@client.command()

async def bugs(ctx):
  
    em = discord.Embed(
        title="Bugs & Future ",
        description="`A bug` is a coding error in a computer program.",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())

    em.set_image(
        url=
        "https://media.discordapp.net/attachments/868094887000690700/880474923884249118/My_Post_1.png?width=644&height=644"
    )
    em.set_thumbnail(
        url=
        "https://media.discordapp.net/attachments/868094887000690700/880475506850553936/unknown.png?width=644&height=644"
    )
    em.add_field(name="Current Bugs 🐛",
                 value="All commands working well ✅",
                 inline=False)
    em.add_field(
        name="Future Updates 🔮",
        value="Adding new pokemon info commands and genhin character builds.",
        inline=False)
    em.add_field(
        name="What to do if you find any bug🐛?",
        value=
        "Join Our Help Server Or Contact the Creator `(Id:-Divyam#0001)` .",
        inline=False)
    await ctx.send(embed=em)




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
    em.add_field(name="Developers", value="Divyam#0001 \nThunder_AB0106💜#4548" , inline=False)
    em.add_field(name="Stats",value=f'Ping :- {round(client.latency *1000)}ms \n Guilds :- {len(client.guilds)} ', inline=False)
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


##Genshin
@client.group(invoke_without_command=True,
              aliases=["GENSHIN", "Genshin", "gs"])
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
        "Use **&help** `<command>` for more information about the command and note that our default prefix is **&**.",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())

    em.set_image(
        url=
        "https://cdn.discordapp.com/attachments/858354774810689557/928949260161019944/standard_5.gif"
    )
    em.add_field(
        name="Change Prefix <a:settings:940198899715555359>",
        value=
        "To change prefix type  `<default prefix>` changeprefix `<new prefix>`. "
    )
    em.add_field(name="Fun <a:fun:940198380309737472>",
                 value="`8Ball,Guess,Imagine,Giveaway,dog,cat,meme`",
                 inline=False)
    em.add_field(name="Info <:Inform:940198203435929710>",
                 value="`Avatar,Serverinfo,info,Stats,Userinfo,poll,tally`",
                 inline=False)
    em.add_field(name="Special <a:Special:940197538810720266>",
                 value="`Reminder,Bugs,Translate,afk,lock,unlock,slowmode`",
                 inline=False)
    em.add_field(name="Anime <:keqing:939052537699512340>",
                 value="`anime,character,animenews`",
                 inline=False)
    
    em.add_field(
        name="Music <a:music:940196835052646411>",
        value=
        "`Connect,Disconnect,Play,Skip,Pause,Resume,Seek <seconds>,Volume <vol>,Loop,Nowplaying,Queue,Equalizer`",
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


@client.group(invoke_without_command=True, aliases=["h", "Help", "HELP"])
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description=
        "Use **&help** `<command>` for more information about the command and note that our default prefix is **&**.",
        colour=discord.Colour.random(),
        timestamp=datetime.utcnow())

    em.set_image(
        url=
        "https://cdn.discordapp.com/attachments/858354774810689557/928949260161019944/standard_5.gif"
    )
    em.add_field(
        name="Change Prefix <a:settings:940198899715555359>",
        value=
        "To change prefix type  `<default prefix>` changeprefix `<new prefix>`. "
    )
    em.add_field(name="Fun <a:fun:940198380309737472>",
                 value="`8Ball,Guess,Imagine,Giveaway,dog,cat,meme`",
                 inline=False)
    em.add_field(name="Info <:Inform:940198203435929710>",
                 value="`Avatar,Serverinfo,info,Stats,Userinfo,poll,tally`",
                 inline=False)
    em.add_field(name="Special <a:Special:940197538810720266>",
                 value="`Reminder,Bugs,Translate,afk,lock,unlock,slowmode`",
                 inline=False)
    em.add_field(name="Anime <:keqing:939052537699512340>",
                 value="`anime,character,animenews`",
                 inline=False)
    
    em.add_field(
        name="Music <a:music:940196835052646411>",
        value=
        "`Connect,Disconnect,Play,Skip,Pause,Resume,Seek <seconds>,Volume <vol>,Loop,Nowplaying,Queue,Equalizer`",
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


@help.command(aliases=["calc", "compute"])
async def Compute(ctx):
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
                 value="`Number 1` - `Number 2` = **Differnce** ",
                 inline=False)
    em.add_field(name="For Multiplication :-",
                 value="`Number 1` * `Number 2` = **Product** ",
                 inline=False)
    em.add_field(name="For Division :-",
                 value="`Number 1` / `Number 2` = **Quotient** ",
                 inline=False)
    em.add_field(name="For Exponential :-",
                 value="`Number 1`^ `Number 2` = **number1^number2** ",
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


extensions=[ 

            'cogs.anime'
            
]
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

client.run('token')

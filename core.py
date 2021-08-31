


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
from random import choice
import datetime
import asyncio
from discord import DefaultAvatar

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

import googletrans

from googletrans import Translator

import math
from webserver import keep_alive

import os

import akinator
from discord.ext import commands
from akinator.async_aki import Akinator

from discord.ext.commands import BucketType


my_default_prefix = "&" 


def get_prefix(client, message): # declare lol
    with open("prefixes.json", "r") as f: # opening the file ofc
        prefixes = json.load(f)
    try:
        prefix = prefixes[str(message.guild.id)] # trying to get the prefix ( if exists )
    except KeyError: # catching the error 
        prefix = my_default_prefix # if no prefix found, setting prefix as default prefix

    return prefix # returning the prefix Ez




client = commands.Bot( command_prefix = get_prefix )

@client.event
async def on_guild_join(guild):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = ">" 
   
    with open("prefixes.json","w") as f:
        json.dump(prefixes,f)


@client.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx,prefix):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix
   
    with open("prefixes.json","w") as f:
        json.dump(prefixes,f)

    await ctx.send(f"The prefix was changed to {prefix}")   

@client.event
async def on_message(msg):
    try:

        if msg.mentions[0] == client.user:
           with open("prefixes.json","r") as f:
                prefixes = json.load(f)
                pre =  prefixes[str(msg.guild.id)] 
        
           await msg.channel.send(f"My prefix for this server is {pre} ")
    
    except:
        pass


    await client.process_commands(msg)







@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'>help ● Watching {len(client.guilds)} servers'))
    print(' Hello I am AutoBot. ')
    client.load_extension('dismusic')
    




@client.event
async def on_command_error(ctx, error):
  if isinstance(error,commands.CommandOnCooldown):
    msg = '**Still on Cooldown**,please try again in ** {:.2f}s **'.format(error.retry_after)
    await ctx.send(msg)




@client.command(aliases=['Ping','PING'],help='Latency')
@commands.cooldown(3,10,commands.BucketType.user)
async def ping(ctx):
    
    message= await ctx.send('🔌`Intialising connection...`')
    await message.edit(content="🛠️`Processing...`")
    
    await message.edit(content=f'🟢 **Pong!  {round(client.latency *1000)  }ms** ')
    




@client.command(aliases=["Stats","STATS"])
@commands.cooldown(3,10,commands.BucketType.user)
async def stats(ctx):
    embed = discord.Embed(title="AutoBot Stats", description="", color=discord.Color.random(),timestamp=datetime.utcnow())
    embed.add_field(name="Server Count", value=  len(client.guilds), inline=False)
    embed.add_field(name="Average Latency", value=round(client.latency *1000),inline=False)
    
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/866949734512853012/871601633061142568/My_Post_3.png?width=606&height=606')


    await ctx.send(embed=embed)





    
@client.command(aliases=['8ball','8Ball'])
@commands.cooldown(3,10,commands.BucketType.user)
async def _8ball(ctx,* , question):
    responses = ["As I see it, yes.",
                 "Ask again later.", 
                 "Better not tell you now.",
                  "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don’t count on it.",
                 "It is certain.",
                 "It is decidedly so.",
                 "Most likely.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Outlook good.",
                 "Reply hazy, try again.",
                  "Signs point to yes.",
                   "Very doubtful.",
                    "Without a doubt.",
                 "Yes.",
                 "Yes – definitely.",
                  "You may rely on it."]
    message= await ctx.send('`Going through database🗄️...`')              
             
    await message.edit(content=f'*Question:* {question}\n**Answer**: {random.choice(responses)}')


@client.command(aliases=['Imagine','IMAGINE'])
@commands.cooldown(3,10,commands.BucketType.user)
async def imagine(ctx):
    responses = ["https://media.discordapp.net/attachments/862895445381218334/871692994955329567/My_Post.png?width=1078&height=606",
                 "https://media.discordapp.net/attachments/862895445381218334/871698288053723136/My_Post_1.png?width=1078&height=606",  
                  "https://media.discordapp.net/attachments/862895445381218334/871710199931621396/My_Post_2.png?width=1078&height=606"         
                                 ]
    message= await ctx.send(' `Imagining...`')
    await message.edit(content=" `10% complete`")
    await message.edit(content=" `50% complete`")
    await message.edit(content=" `100% complete`")
    await message.edit(content=f' {random.choice(responses)}')












@client.command(aliases=["Serverinfo","aboutserver","server"])
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description="",
      color=discord.Color.random(),
      timestamp=datetime.utcnow()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=False)
  embed.add_field(name="Server ID", value=id, inline=False)
  embed.add_field(name="Region", value=region, inline=False)
  embed.add_field(name="Member Count", value=memberCount, inline=False)

  await ctx.send(embed=embed)




@client.command(aliases=["hello","HI", "Hi", "Hello" , "HELLO", "こんにちは" , "नमस्ते", "你好"])
async def hi(ctx):
    embed = discord.Embed(title="Hello", description="I am Autobot", color=discord.Color.random())
    embed.add_field(name="Wassup!", value= "Nice to meet you")
    
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866949734512853012/866949844543209502/unknown.png")
    
    await ctx.send(embed=embed)



@client.command(aliases=['Jinx','JINX','JiNx','jInX'])
async def jinx(ctx):
    embed = discord.Embed(title="Jinx", description="Jinx we send the same message!", color=discord.Color.random())
    embed.add_field(name="😂", value= ":)")
    
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/866949734512853012/866961591512465408/JINX__1_-removebg-preview.png")
    
    await ctx.send(embed=embed)



afkdict = {}
@client.command(name = "afk", brief = "Away From Keyboard",
                description = "I'll give you the afk status and if someone pings you before you come back, I'll tell "
                              "them that you are not available. You can add your own afk message!")
async def afk(ctx, message = "They didn't leave a message!"):
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
                await message.channel.send(f"Oh noes! {member} is afk💤. {afkmsg}")
                
                
    await client.process_commands(message)
                

@commands.command(name="test")
async def test(ctx):
    message = 'Hi'
    msg = await ctx.send(message)
    await ctx.message.delete() # Deletes the users message
    await asyncio.sleep(5) # you want it to wait.
    await msg.delete() # Deletes the message the bot sends.
 
client.add_command(test)






@client.command(aliases=['lol','Lol','LoL'])
async def LOL(ctx):
    embed = discord.Embed(title="LOL", description="Laugh Out Loud", color=discord.Color.random())
    
    
    embed.set_image(url='https://cdn.discordapp.com/attachments/866949734512853012/867307009895956540/JINX-1--unscreen.gif')
    
    await ctx.send(embed=embed)











@client.command(aliases=['Github','GitHub','GITHUB'])
async def github(ctx):
    embed = discord.Embed(title="Github", description="Our Community!", color=discord.Color.random())
    embed.add_field(name="Visit Me", value= "https://github.com/DivyamSamarwal")
    embed.add_field(name="About me",value="I am Musical Pieces (Software Dev) I am owner of non profit organization named PokeMedia... Nowadays, I am working on my projects like Autobot and PokeMedia. I mostly use python for coding bots..")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/865177734510411816/867300427153670144/GitHub-logo.png?width=1078&height=606")
    embed.set_image(url='https://media.discordapp.net/attachments/866949734512853012/868778562763759626/circle-cropped.png')


    await ctx.send(embed=embed)









@client.command(aliases=["Invite","INVITE"])
async def invite(ctx):
    embed = discord.Embed(title="Invite", description="Link to invite me", color=discord.Color.random(),timestamp=datetime.utcnow())
    embed.add_field(name="AutoBot", value= "https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=2147875862&scope=bot")
    
    
    embed.set_image(url='https://media.discordapp.net/attachments/866949734512853012/871601633061142568/My_Post_3.png?width=606&height=606')


    await ctx.send(embed=embed)



@client.command(aliases=["Avatar","AVATAR","AV","av"])
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)



datetime.utcnow()

@client.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me","Reminder"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
    embed.set_footer(text="If you have any questions, suggestions or bug reports, please join our support Discord Server: Link in help command.", icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
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
        embed.add_field(name='Warning',
                        value='Please specify a proper duration, send `help reminder` for more information.')
    elif seconds < 180:
        embed.add_field(name='Warning',
                        value='You have specified a too short duration!\nMinimum duration is 3 minutes.')
    elif seconds > 7776000:
        embed.add_field(name='Warning', value='You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        await ctx.send(f"Alright, I will remind {user} about {reminder} in {counter}.")
        await asyncio.sleep(seconds)
        await ctx.send(f"Hi, you asked me to remind you about {user} {reminder} {counter} ago.")
        return
    await ctx.send(embed=embed)






@client.command(aliases=["HAPPY","Happy"])
async def happy(ctx):
    test = discord.Embed(title=f"This avatar seems unsual✨...", colour = discord.Color.random(),timestamp=datetime.utcnow())
    test.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    test.set_image(url=ctx.author.avatar_url)
    await ctx.send(embed=test)


@client.command(aliases=["dm","Dm", "Direct Message, dM"])
async def DM(ctx, user: discord.User, *, message=None):
    message = message or f"Hello My friend  {user}  User didn't leave message.."
    await user.send(message)


@client.command(aliases=["t","Translate","T","tl","TL","Tl"])
async def translate(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)







@client.command(aliases=["Calculator","calc","compute","COMPUTE","CALC"])
async def Compute(ctx):
    def check(m):
        return len(m.content) >= 1 and m.author != client.user

    await ctx.send("Number 1: ")
    number_1 = await client.wait_for("message", check=check)
    await ctx.send("Operator: ")
    operator = await client.wait_for("message", check=check)
    await ctx.send("number 2: ")
    number_2 = await client.wait_for("message", check=check)
    try:
        number_1 = float(number_1.content)
        operator = operator.content
        number_2 = float(number_2.content)
    except:
        await ctx.send("invalid input")
        return
    output = None
    if operator == "+":
        output = number_1 + number_2
    elif operator == "-":
        output = number_1 - number_2
    elif operator == "/":
        output = number_1 / number_2
    elif operator == "*":
        output = number_1 * number_2
    elif operator == "**":
        output = number_1 ** number_2 
    elif operator == "//":
        output = number_1 // number_2
             
    else:
        await ctx.send("invalid input")
        return
    await ctx.send("Answer: " + str(output))



 
@client.command(aliases=["Userinfo","ui","UserInfo"])
async def userinfo(ctx, member : discord.Member = None):
    member = ctx.author if not member else member
    roles =[role for role in member.roles]

    embed = discord.Embed(colour=discord.Color.random() , timestamp =ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:-", value= member.id,inline=False)
    embed.add_field(name="Guild Name:-",value= member.display_name,inline=False)

    embed.add_field(name="Created At:-",value= member.created_at.strftime("%a , %#d %B %Y, %I:%M %p UTC"),inline=False)
    embed.add_field(name="Joined At:-",value= member.joined_at.strftime("%a , %#d %B %Y, %I:%M %p  UTC"),inline=False)

    embed.add_field(name=f"Roles:- ({len(roles)})", value="".join([role.mention for role in roles]),inline=False)
    embed.add_field(name="Top Role:-",value= member.top_role.mention,inline=False)
    embed.add_field(name="Bot?",value=member.bot,inline=False)

    await ctx.send(embed=embed)

    
    
#   ----------------AKINATOR 



def w(name, desc, picture):
    embed_win = discord.Embed(title=f"It's {name} ({desc})! Was I correct?",
                              colour = discord.Color.random())
    embed_win.set_image(url=picture)
    return embed_win


aki = Akinator()
emojis_c = ['✅', '❌', '🤷', '👍', '👎', '⏮', '🛑']
emojis_w = ['✅', '❌']




@client.command(name='guess', aliases=["aki","akinator"])
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
                q = await aki.start_game(language=f'en_{extra}',
                                         child_mode=True)
            else:
                title_error_three = 'This game mode does not exist'
                desc_error_three = 'Use **.help** to see a list of all the game modes available'
                embed_var_three = discord.Embed(title=title_error_three,
                                                description=desc_error_three,
                                                colour = discord.Color.random())
                await ctx.reply(embed=embed_var_three)
                return

            embed_question = discord.Embed(
                title=
                'Tip : Wait until all emojis finish being added before reacting'
                ' or you will have to unreact and react again',
                colour = discord.Color.random())
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
                    colour = discord.Color.random())
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
                    colour = discord.Color.random())
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
                                       colour = discord.Color.random())
            await ctx.reply(embed=embed_loss)
            return

        if str(s) == emojis_w[0]:
            embed_win = discord.Embed(
                title='Great, guessed right one more time!',colour = discord.Color.random())
            await ctx.reply(embed=embed_win)
        elif str(s) == emojis_w[1]:
            for times in aki.guesses:
                desc_loss = desc_loss + times['name'] + '\n'
            title_loss = 'No problem, I will win next time! But here is a list of all the people I had in mind :'
            embed_loss = discord.Embed(title=title_loss,
                                       description=desc_loss,
                                       colour = discord.Color.random())
            await ctx.reply(embed=embed_loss)
    

#music

client.lava_nodes = [ 
    {
      'host' : 'lava.link',
      'port' :  80 ,
      'rest_uri': f'http://lava.link:80',
      'identifier': 'MAIN',
      'password' : 'anything',
      'region' :'singapore'
    }

]





#------BUGS

@client.command(aliases=['Bugs','BUGS','futureupdates'])
async def bugs(ctx):
    em = discord.Embed(title = "Bugs & Future" , description = "`A bug` is a coding error in a computer program.", colour=discord.Colour.random(),timestamp=datetime.utcnow())
   
    em.set_image(url="https://media.discordapp.net/attachments/868094887000690700/880474923884249118/My_Post_1.png?width=644&height=644")
    em.set_thumbnail(url="https://media.discordapp.net/attachments/868094887000690700/880475506850553936/unknown.png?width=644&height=644")
    em.add_field(name="Current Bugs 🐛", value= "Bot stucks between the guess game.",inline=False)
    em.add_field(name="Future Updates 🔮",value="Trying to simplify bot commands use and updating music commands...",inline=False)
    em.add_field(name="What to do if you find any bug🐛?",value="Join Our Help Server Or Contact the Creator `(Id:-MusicalPieces◥▶_◀◤#0009)` .",inline=False)
    await ctx.send(embed = em) 



























#help 


client.remove_command("help") 

@client.group(invoke_without_command = True, aliases = ["h", "Help", "HELP"])
async def help(ctx):
    em = discord.Embed(title = "Help" , description = "Use **>help** `<command>` for more information about the command and note that our default prefix is **>**.", colour=discord.Colour.random(),timestamp=datetime.utcnow())
   
    em.set_image(url="https://media.discordapp.net/attachments/866949734512853012/875315601671876648/0c6f19d924387f617542d93fe3bb0f1e120b4b9ddd39dbd5f95ef0ae07d42a24.gif")
    em.add_field(name="Change Prefix", value="To change prefix type  `<default prefix>` changeprefix `<new prefix>`. ")
    em.add_field(name="Fun 🎁", value= "`8Ball,Hi,Jinx,Lol,Happy,Guess,Imagine`",inline=False)
    em.add_field(name="Info㊙️",value="`Avatar,Serverinfo,Github,Compute,Stats,Userinfo`",inline=False)
    em.add_field(name="Special✨",value="`Reminder,Invite,Bugs,Dm,Translate,afk`",inline=False)
    em.add_field(name="Music🎵",value="`Connect,Disconnect,Play,Skip,Pause,Resume,Seek <seconds>,Volume <vol>,Loop,Nowplaying,Queue,Equalizer`")
    em.add_field(name="AutoBot Help ❓",value="https://discord.gg/2uah9Bc5XJ",inline=False)
    em.add_field(name="Patreon 💖",value="https://www.patreon.com/AutoBot0521",inline=False)
    
    em.set_footer(text="Created by MusicalPieces◥▶_◀◤#0009")
    await ctx.send(embed = em) 






#help inbuilds

@help.command(aliases=["calc","compute"])
async def Compute(ctx):
    em=discord.Embed(title="Calculator",description=" It is something used for making mathematical calculations  ", colour=discord.Colour.random(),timestamp=datetime.utcnow())
    em.add_field(name="For Addition :-", value="`Number 1` + `Number 2` = **Sum** ",inline=False)
    em.add_field(name="For Subtraction :-", value="`Number 1` - `Number 2` = **Differnce** ",inline=False)
    em.add_field(name="For Multiplication :-", value="`Number 1` * `Number 2` = **Product** ",inline=False)
    em.add_field(name="For Division :-", value="`Number 1` / `Number 2` = **Quotient** ",inline=False)
    em.add_field(name="For Exponential :-", value="`Number 1`^ `Number 2` = **number1^number2** ",inline=False)
    em.add_field(name="For Remainder :-", value="`Number 1` // `Number 2` = **Remainder If not fully divisible.** ",inline=False)
    await ctx.send(embed=em)











@help.command()
async def ping(ctx):
    em=discord.Embed(title="Ping",description="Shows the latency of the bot", colour=discord.Colour.random())
    em.add_field(name="**Syntax**", value="`Bot Prefix` ping")
    await ctx.send(embed=em)

@help.command()
async def afk(ctx):
    em=discord.Embed(title="Afk",description="Away from keys", colour=discord.Colour.random())
    em.add_field(name="**Syntax**", value="   `Bot Prefix` afk")
    await ctx.send(embed=em)

@help.command()
async def _8ball(ctx):
    em=discord.Embed(title="8ball",description="Your Question and Bot Answer", colour=discord.Colour.random())
    em.add_field(name="**Syntax**", value="   `Bot Prefix` <command name> `question`")
    await ctx.send(embed=em)


@help.command(aliases=["tl","TL"])
async def translate(ctx):
    em=discord.Embed(title="Translate",description="Translates one language to other", colour=discord.Colour.random())
    em.add_field(name="**Syntax**", value="<command> <language you want to translate > input ")
    
    await ctx.send(embed=em)

@help.command()
async def reminder(ctx):
    em=discord.Embed(title="Reminder",description="Reminds at specific time ", colour=discord.Colour.random())
    em.add_field(name="**Syntax**", value="`<prefix> command` duration(3 minutes to  90 days) `<your message>` " )
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
    embed_var_helpme = discord.Embed(description=desc_helpme, colour = discord.Color.random())
    await ctx.send(embed=embed_var_helpme)



keep_alive()




client.run('')





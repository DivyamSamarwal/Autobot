

from asyncio.tasks import wait
from time import time
import discord
import random
from discord import colour
from discord import embeds
from discord import message
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
    await client.change_presence(status=discord.Status.online, activity=discord.Game(' AutoBot ● Prefix (>)'))
    print(' Hello I am AutoBot. ')





@client.command(aliases=['Ping','PING'],help='Latency')
async def ping(ctx):
    
    message= await ctx.send('🔌`Intialising connection...`')
    await message.edit(content="🛠️`Processing...`")
    
    await message.edit(content=f'🟢 **Pong!  {round(client.latency *1000)}ms**')
    

    
@client.command(aliases=['8ball','8Ball'])
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

@client.command(aliases=["Serverinfo"])
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
      description=description,
      color=discord.Color.random()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

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
    embed = discord.Embed(title="Invite", description="Link to invite me", color=discord.Color.random())
    embed.add_field(name="AutoBot", value= "https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=2147875862&scope=bot")
    
    
    embed.set_image(url='https://media.discordapp.net/attachments/866949734512853012/871601633061142568/My_Post_3.png?width=606&height=606')


    await ctx.send(embed=embed)



@client.command(aliases=["Avatar","AVATAR"])
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
    embed.set_footer(text="If you have any questions, suggestions or bug reports, please join our support Discord Server: link hidden", icon_url=f"{client.user.avatar_url}")
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
                        value='Please specify a proper duration, send `reminder_help` for more information.')
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
    test = discord.Embed(title=f"This avatar seems unsual✨...", colour = discord.Color.random())
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




#help 


client.remove_command("help") 

@client.group(invoke_without_command = True, aliases = ["h", "Help", "HELP"])
async def help(ctx):
    em = discord.Embed(title = "Help" , description = "Use **>help** `<command>` for more information about the command and note that our default prefix is **>**.", colour=discord.Colour.random())
   
    em.set_image(url="https://media.discordapp.net/attachments/866949734512853012/875315601671876648/0c6f19d924387f617542d93fe3bb0f1e120b4b9ddd39dbd5f95ef0ae07d42a24.gif")
    em.add_field(name="Change Prefix", value="To change prefix type  <default prefix> changeprefix <new prefix>. ")
    em.add_field(name="Fun 🎁", value= "`8Ball,Hi,Jinx,Lol`",inline=False)
    em.add_field(name="Info㊙️",value="`Avatar,Serverinfo,Github,Happy`",inline=False)
    em.add_field(name="Special✨",value="`Reminder,Invite,Imagine,Dm,Translate,afk`",inline=False)
    em.add_field(name="AutoBot Help ❓",value="https://discord.gg/jKbtPHJ9Ef",inline=False)
    em.add_field(name="Patreon 💖",value="https://www.patreon.com/musicalpieces",inline=False)
    
    em.set_footer(text="Created by MusicalPieces◥▶_◀◤#0009")
    await ctx.send(embed = em) 






#help inbuilds
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


@help.command()
async def translate(ctx):
    em=discord.Embed(title="Translate",description="Translates one language to other", colour=discord.Colour.random())
    em.add_field(name="**Syntax**", value="<command> <language you want to translate > input ")
    
    await ctx.send(embed=em)

@help.command()
async def reminder(ctx):
    em=discord.Embed(title="Reminder",description="Reminds at specific time ", colour=discord.Colour.random())
    em.add_field(name="**Syntax**", value="`<prefix> command` duration(3 minutes to  90 days) `<your message>` " )
    await ctx.send(embed=em)







client.run('Token')




import discord
import random
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands, tasks
from random import choice
import datetime
import asyncio
from discord import DefaultAvatar

from urllib import parse, request
import re


from discord.ext.commands.core import command


client = commands.Bot( command_prefix = '&' )

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(' AutoBot/Prefix (&)'))
    print(' Hello I am AutoBot. ')

@client.command(help='Latency')
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency *1000)}ms')



@client.command(aliases=['8ball','test'])
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
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')









@client.command()
async def kick( ctx , member : discord.Member,*, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban( ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)





@client.command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server", timestamp=datetime.datetime.utcnow(), color=discord.Color.random())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/862599394712354831/866541849635323934/unknown.png?width=606&height=606")

    await ctx.send(embed=embed)




@client.command()
async def hi(ctx):
    embed = discord.Embed(title="Hello", description="I am Autobot", color=discord.Color.random())
    embed.add_field(name="Wassup!", value= "Nice to meet you")
    
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866949734512853012/866949844543209502/unknown.png")
    
    await ctx.send(embed=embed)



@client.command()
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
        await ctx.send('Welcome back!🔛 You are no longer afk.')

    else:
        afkdict[ctx.message.author] = message
        await ctx.send("You are now afk💤!")


@client.event
async def on_message(message):
    global afkdict

    for member in message.mentions:  
        if member != message.author:  
            if member in afkdict:  
                afkmsg = afkdict[member]  
                await message.channel.send(f"Oh noes! {member} is afk💤. {afkmsg}")
    await client.process_commands(message)






@client.command()
async def data(ctx):
    embed = discord.Embed(title="Data", description="Send Your Data Here!", color=discord.Color.random())
    embed.add_field(name="Fill this Form", value= "https://forms.gle/JuSvVbrVfWZmsaen8")
    
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/866949734512853012/867051963023360030/BigData.png")
    
    await ctx.send(embed=embed)






@client.command()
async def LOL(ctx):
    embed = discord.Embed(title="LOL", description="Laugh Out Loud", color=discord.Color.random())
    
    
    embed.set_image(url='https://cdn.discordapp.com/attachments/866949734512853012/867307009895956540/JINX-1--unscreen.gif')
    
    await ctx.send(embed=embed)











@client.command()
async def github(ctx):
    embed = discord.Embed(title="Github", description="Our Community!", color=discord.Color.random())
    embed.add_field(name="Visit Our Community", value= "https://github.com/DivyamSamarwal/Autobot")
    
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/865177734510411816/867300427153670144/GitHub-logo.png?width=1078&height=606")
    embed.set_image(url='https://images-ext-1.discordapp.net/external/WphBG90KADvKReGXoSZ1VqjCx3vI3Lgm0LgBnO27AXs/%3Fwidth%3D606%26height%3D606/https/media.discordapp.net/attachments/862599394712354831/866541849635323934/unknown.png?width=375&height=375')


    await ctx.send(embed=embed)





@client.command()
async def credits(ctx):
    embed = discord.Embed(title="Credits", description="Created By Musical Pieces", color=discord.Color.random())
    
    
    
    embed.set_image(url='https://media.discordapp.net/attachments/866949734512853012/867312649287761920/unnamed.png')


    await ctx.send(embed=embed)



@client.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite", description="Link to invite me", color=discord.Color.random())
    embed.add_field(name="AutoBot", value= "https://discord.com/api/oauth2/authorize?client_id=858965828716331019&permissions=2147875862&scope=bot")
    
    
    embed.set_image(url='https://media.discordapp.net/attachments/866949734512853012/867614971113898014/9833ce074d47bbc360a05df6c49e0500.png')


    await ctx.send(embed=embed)



@client.command()
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)




client.run('Token')






import discord
import random
from discord.ext import commands, tasks
from random import choice


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







@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(' Oops! Command does not exist.')


@client.command()
async def kick( ctx , member : discord.Member,*, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban( ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)


@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**','**Bye.. I am busy**']
    await ctx.send(choice(responses))


@client.command(name='jinx', help='Jinx')
async def jinx(ctx):
    responses = ['***Jinx*** ', '***Jinx we send the same message!***', '***What??***', '**Uh,Jinx**']
    await ctx.send(choice(responses))


@client.command(name='data', help='Send Your Data')
async def data(ctx):
    responses = 'Fill Our Form here, https://forms.gle/JuSvVbrVfWZmsaen8 '
    await ctx.send(responses)



@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))


@client.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by `Musical Pieces`')

@client.command(name='creditz', help='This command returns the TRUE credits')
async def creditz(ctx):
    await ctx.send('**No one but me, lozer!**')    



client.run('ODU4OTY1ODI4NzE2MzMxMDE5.YNl0RA.X5NelU5FRkoynN8_vR-LyK8w06s')



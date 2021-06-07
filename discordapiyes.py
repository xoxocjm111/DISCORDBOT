import discord
from datetime import date
from discord.ext import commands, tasks
import webbrowser
import os
import time

token = 'NzMzODI4Njc3OTI5Nzk1NjQ0.XxI1Ng.i_xTX-sSVwD2e32UnCV51-CJA_Y'

os.system('clear')

print('Initializing Client...')


#init client
client = commands.Bot(command_prefix = '?')

client.remove_command('help')
#displays date
today = date.today()

#Displays when bot is ready
@client.event
async def on_ready():
  print('Client Ready..')



  print("""
  APCS PROJ.

  just a simple bot for Discord.

  what it can do:

  It can open web pages on my pc and if you use ?annoychris (type something here) in my discord bot spam channel it will open a webpage on my browser.

  https://discord.gg/THDBHFbvaB LINK TO MY DISCORD
  """)
  time.sleep(2)



  print(" ")

  print('[1] Restart')

  print('[2] Exit')
  print(" ")

  usrImpt = input('dbbot > ')


  if usrImpt == '1':
    os.system('python3 discordapiyes.py')

  if usrImpt == '2':
    exit()

#Sends input back to user
@client.command()
async def send_input(ctx, arg):
  await ctx.send(arg)


@client.command()
async def ping(ctx):
  await ctx.send(f'The latency is {round(client.latency * 1000)}ms')

@client.command()
async def date(ctx):
  await ctx.send(today)

@client.command()
async def tellmeajoke(ctx):
  await ctx.send('no')

@client.command()
#im going to hate this fucking feature
async def annoychris(ctx, arg):
  os.system('sensible-browser https://google.com/search?q=' + arg)
  await ctx.send('FUCK YOU')

@client.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author

  embed = discord.Embed(
    colour = discord.Colour.orange()
  )

  embed.set_author(name='Help')
  embed.add_field(name='?help', value='Show list of all commands to user', inline=False)
  embed.add_field(name='?ping', value='Return ping back to user', inline=False)
  embed.add_field(name='?date', value='Show date to user', inline=False)
  embed.add_field(name='?tellmeajoke', value='Tells the user a joke', inline=False)
  embed.add_field(name='?send_input', value='Any args the user submits, the bot sends back', inline=False)
  embed.add_field(name='?annoychris', value='Opens my web browser to any argument you type after ?annoychris (arg goes here), also fuck you')



  await ctx.send(author, embed=embed)

@client.command()
async def clear(ctx, number=5):
  await ctx.channel.purge(limit=number)


client.run(token)

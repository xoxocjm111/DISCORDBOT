import discord
from datetime import date
from discord.ext import commands, tasks
import webbrowser
import os

token = 'NzMzODI4Njc3OTI5Nzk1NjQ0.XxI1Ng.xf4MFn-epZDZG9wk5B6UYG7yYxc'

#init client
client = commands.Bot(command_prefix = '?')

client.remove_command('help')
#displays date
today = date.today()

#Displays when bot is ready
@client.event
async def on_ready():
  print('Bot is ready')

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

client.run(token)

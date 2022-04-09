import discord
import os
from datetime import datetime, date, timedelta
from pytz import timezone
import calendar
from keep_alive import keep_alive

#set client
client = discord.Client()

#define timezone and weekday for U.S. users
zone = timezone('Pacific/Gambier')
day = datetime.now(tz=zone).strftime('%A')

#When logging into repl.it
@client.event
async def on_ready():
  print('You have logged in as {0.user}'.format(client))

#Initiate message return system
@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
#!Hello command
  if message.content.startswith('!hello'):
    await message.channel.send('Ad Astra Abyssosque! Welcome to the Adventurers\' Guild.') 
#!Daily command
  if message.content.startswith('!daily'):
    if day == 'Monday' or day == 'Thursday':
      await message.channel.send(file=discord.File('monday.png'))
    if day == 'Tuesday' or day == 'Friday':
      await message.channel.send(file=discord.File('tuesday.png'))
    if day == 'Wednesday' or day == 'Saturday':
      await message.channel.send(file=discord.File('wednesday.png'))
    if day == 'Sunday':
      await message.channel.send(file=discord.File('sunday.png'))

#Uptime Robot
keep_alive()
#Connect to Discord Bot
client.run(os.getenv('TOKEN'))
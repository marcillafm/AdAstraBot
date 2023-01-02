import discord
import os
from datetime import datetime, date, timedelta
from pytz import timezone
import calendar
from dotenv import load_dotenv
from PIL import Image
import urllib.request

load_dotenv()

#set client
client = discord.Client()

#define timezone and weekday for U.S. users
zone = timezone('Pacific/Gambier')

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
    day = datetime.now(tz=zone).strftime('%A')
    if day == 'Monday' or day == 'Thursday':
      await message.channel.send('https://raw.githubusercontent.com/marcillafm/AdAstraBot/master/mon_thurs1.png')
      await message.channel.send('https://raw.githubusercontent.com/marcillafm/AdAstraBot/master/mon_thurs2.png')
    if day == 'Tuesday' or day == 'Friday':
      await message.channel.send('https://raw.githubusercontent.com/marcillafm/AdAstraBot/master/tue_fri.png')
    if day == 'Wednesday' or day == 'Saturday':
      await message.channel.send('https://raw.githubusercontent.com/marcillafm/AdAstraBot/master/wed_sat.png')
    if day == 'Sunday':
      await message.channel.send('https://raw.githubusercontent.com/marcillafm/AdAstraBot/master/sun.png')

#Connect to Discord Bot
client.run(os.getenv('TOKEN'))
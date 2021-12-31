import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
    
  if message.content == 'hello':
    await message.add_reaction('\U0001F44B')

  if message.content == 'Hello':
    await message.add_reaction('\U0001F44B')

  if message.content == 'hi':
    await message.add_reaction('\U0001F44B')

  if message.content == 'Hi':
    await message.add_reaction('\U0001F44B')

  if message.content == 'lol':
    await message.add_reaction('\U0001F601') 

  if message.content == 'lmao':
    await message.add_reaction('\U0001F602') 

  if message.content == 'LMAO':
    await message.add_reaction('\U0001F602') 

  if message.content == '+help':
    await message.channel.send('Hi Im NotRealSean bot\nHere are some command you can use for now\n+help = See command\n+rng = Random number from 1 to 100\n+luck = Tell how lucky you are(3%)')
    await message.add_reaction('\U0001F44C')

  if message.content == '+tenshichanisthebest':
    await message.channel.send('Thank you onii-chan\U0001F499')
    await message.add_reaction('\U0001F499')
  
  if message.content == '+rng':
    await message.channel.send(int(random.uniform(1,100)))
   
  if message.content == '+luck':
    luck = random.uniform(1,100)
    luck = int(luck)
    if luck <= 3:
      await message.channel.send('You are lucky today')
    else:
      await message.channel.send('You are unlucky!')

client.run(os.getenv('TOKEN'))
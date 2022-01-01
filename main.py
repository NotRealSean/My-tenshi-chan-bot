import discord
import os
import random
import time

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user} is now online!'.format(client))

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

  if message.content == 'LOL':
    await message.add_reaction('\U0001F601') 

  if message.content == 'lmao':
    await message.add_reaction('\U0001F602') 

  if message.content == 'LMAO':
    await message.add_reaction('\U0001F602') 

  if message.content == 'poi':
    await message.channel.send('ぽい！')
  
  if message.content == 'POI':
    await message.channel.send('ぽい！')

  if message.content == 'tenshi chan is the best':
    await message.channel.send('Thank you onii-chan\U0001F499')
    await message.add_reaction('\U0001F499')

  if message.content == '+help':
    await message.channel.send('Hi Im NotRealSean bot\nHere are some command you can use for now\n-------------------------------------------------------\n+help = See command\n+rng = Random number from 1 to 1000\n+luck = Tell how lucky you are(3%)\n+luck10 = Do 10 rolls of +luck\n+digits = \U0001F440\n+lottery = \U0001F44D\n+pray = Pray why not (～￣▽￣)～ \n-------------------------------------------------------')
    await message.add_reaction('\U0001F44C')

  if message.content == '+tenshichanisthebest':
    await message.channel.send('Thank you onii-chan\U0001F499')
    await message.add_reaction('\U0001F499')
  
  if message.content == '+rng':
    await message.channel.send(int(random.uniform(1,1000)))
   
  if message.content == '+luck':
    luck = random.uniform(1,100)
    luck = int(luck)
    if luck <= 3:
      await message.channel.send('You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('You are unlucky better luck next time \U0001F494 ')

  if message.content == '+luck10':
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('1.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('1.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('2.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('2.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('3.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('3.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('4.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('4.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('5.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('5.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('6.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('6.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('7.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('7.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('8.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('8.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('9.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('9.You are unlucky better luck next time \U0001F494 ')
    time.sleep(1)
    Rluck = random.uniform(1,100)
    Rluck = int(Rluck)
    if Rluck <= 3:
      await message.channel.send('10.You are very lucky congratulations!\U0001F499')
    else:
      await message.channel.send('10.You are unlucky better luck next time \U0001F494 ')

  if message.content == '+digits':
    digits = random.uniform(100000,385000)
    digits = int(digits)
    await message.channel.send(digits)
    await message.add_reaction('\U0001F440')

  if message.content == '+lottery':
    await message.channel.send(int(random.uniform(100000,999999)))
    await message.add_reaction('\U0001F44D')

  if message.content == '+pray':
    await message.channel.send('\U0001F614\n\U0001F64F')
    await message.add_reaction('\U0001F64F')


client.run(os.getenv('TOKEN'))
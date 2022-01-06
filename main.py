import discord
import os
import random
import time
import datetime

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user} is ready to see you <3'.format(client))
  print('current version : 1.10.52')  
  

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

  if message.content == 'Tenshi chan is the best':
    await message.channel.send('Thank you onii-chan\U0001F499')
    await message.add_reaction('\U0001F499')

  if message.content == 'ok':
    await message.add_reaction('\U0001F44C')

  if message.content == 'Ok':
    await message.add_reaction('\U0001F44C')

  if message.content == 'OK':
    await message.add_reaction('\U0001F44C')

  if message.content == '+help':
    await message.channel.send('Hi Im Tenshi\nNice to meet you\nHere are some command you can use for now\n-------------------------------------------------------\n+help = See command\n+rng = Random number from 1 to 1000\n+luck = Tell how lucky you are(3%)\n+luck10 = Do 10 rolls of +luck\n+digits = \U0001F440\n+pray = Pray why not (～￣▽￣)～ \n+loli = Try it I dare you\n+ownerfact = Facts about owner\n+event = Tell you about today event\n-------------------------------------------------------\nCurrent version - 1.10.52')
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

  if message.content == '+pray':
    await message.channel.send('\U0001F614\n\U0001F64F')
    await message.add_reaction('\U0001F64F')
  
  if message.content == '+loli':
    loli = random.uniform(1,10)
    loli = int(loli)
    if loli == 1:
      await message.channel.send('mochi mochi fbi-san...')
    if loli == 2:
      await message.channel.send('\U0001F628')
    if loli == 3:
      await message.channel.send('FBI-SAN LOLICON IS HERE!')
    if loli == 4:
      await message.channel.send('+loli command not found please try again.')
    if loli == 5:
      await message.channel.send('404 Tenshi chan found an error please stay turned.')
    if loli == 6:
      await message.channel.send('So... nii-san is lolicon i see')
    if loli == 7:
      await message.channel.send('Nii-san... pervert!')
    if loli == 8:
      await message.channel.send('P-please dont eat me nii-san')
    if loli == 9:
      await message.channel.send('NII-SAN!?!')
    if loli == 10:
      await message.channel.send('Nii-san... can you wait me grown up a little bit please\U0001F499')

  if message.content == '+ownerfact':
    fact = random.uniform(1,10)
    fact = int(fact)
    if fact == 1:
      await message.channel.send('My owner is new to coding')
    if fact == 2:
      await message.channel.send('His favorite character is Hinanawi Tenshi')
    if fact == 3:
      await message.channel.send('He is lazy sometimes but when he want to do something he will over do it')
    if fact == 4:
      await message.channel.send('My owner like to learn japanese')
    if fact == 5:
      await message.channel.send('He like to eaat omelette')
    if fact == 6:
      await message.channel.send('He dont like to talk to people that he dont know')
    if fact == 7:
      await message.channel.send('He like to play ryhthm game')
    if fact == 8:
      await message.channel.send('<3')
    if fact == 9 :
      await message.channel.send('He like gacha game(thats not gacha cringe)')
    if fact == 10:
      await message.channel.send('He is single')
  
  if message.content == '+event':
    Today = datetime.datetime.now()
    await message.channel.send(Today)
    await message.channel.send('Today has no special event\U0001F613')



client.run(os.getenv('TOKEN'))
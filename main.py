import pickle
import random
import discord

# loading and preparing data 
insults_list = pickle.load(open("insult_list.pickle", 'rb'))
num_insults = len(insults_list) - 1

# starting a up discord.py and preparing the client
client = discord.Client()


def insult_article(insult):
    if insult[0] == 'a':
        article = 'an'
    else:
        article = 'a'

    return article

def insult_decree(name):
  insult = insults_list[random.randint(0, num_insults)]

  decree = "{} {} {}".format(name, insult_article(insult), insult)

#    decree = name + " is" + insult_article(insult) + insult

  return decree


@client.event
async def on_ready():
  print('sup fucker')
  

@client.event
async def on_message(message): 
  if message.author == client.user:
    return
  
  if message.content.startswith('bully '):
    bitch = message.content[5:]
    await message.channel.send(insult_decree(bitch))


client.run("OTcwNzI3NzM3Mjg5NDc4MjE1.YnAKpw.dqmSfgWTGtpCgSBuz1khiW62Y0M")
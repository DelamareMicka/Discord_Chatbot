# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:38:51 2020

@author: Icecrow
"""

step = 0
import nest_asyncio
import discord
import logging
nest_asyncio.apply()
from self_chat import chatbot_response_b
import tensorflow as tf
from random import randint
#from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re
from deep_translator import GoogleTranslator
#from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
from transformers import CamembertModel, CamembertTokenizer
#from transformers import XLMTokenizer, XLMWithLMHeadModel
print('library charged')
tokenizer = CamembertTokenizer.from_pretrained("camembert-base")
model = CamembertModel.from_pretrained("camembert-base")


print("model charged")
#tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large") 
#model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")  # microsoft/DialoGPT-large
model.eval()
client = discord.Client()
chat_history_ids = []

print('test')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global step
    ou = re.search(r"\best\s(où|ou) ?", message.content)
    calendar=re.search( r"calendrier|calend", message.content)
    appel=re.search( r"appel|apel", message.content)
    cafe=re.search( r"caf|cof", message.content)
    reprend=re.search( r"reprend|fait", message.content)
    boulot=re.search( r"boulot|boulo|taf", message.content)
    deplacement=re.search( r"deplacement|etrangé|étranger|etranger|déplacement", message.content)
    postuler=re.search( r"postul", message.content)
    
    if postuler:
        await message.channel.send("Non mais je soummet ma candidature à ce qui me plait en faite ? J'ai le droit ? ")
    if deplacement:
        await message.channel.send("ça c'est un problème, je deteste voyager ! Pas envie de me retrouver à New York ou en Chine")
    if boulot:
        await message.channel.send("Toujours au chômage, je commence à regarder les cdi en alternance pour technicien de maintenance ")
    if reprend:
        await message.channel.send("ouais, ce que j'ai fais ")
    if appel:
        await message.channel.send("Flemme, j'ai le nez bouché, j'respire par la bouche, flemme de parler")
    if calendar:
        await message.channel.send("Pas besoin de ça! Je vois pas l'interêt d'un calendrier, le sapin c'est festif ! Pas le calendrier ! ")
    
    if ou:
        await message.channel.send('Oh putain ! Totalement zappé')
    elif message.content.startswith('*'):
        print(message.content)
        text=message.content
        transl= GoogleTranslator(source='auto', target='en').translate(text)  # output -> Weiter so, du bist großartig
        to_send=chatbot_response_b(step=step,user=transl)
        to_send = GoogleTranslator(source='auto', target='fr').translate(to_send)
        print(to_send)
        try:
            await message.channel.send(to_send)
        except:
            await message.channel.send("no response...")

    if message.author == client.user:
        return
    if message.content.startswith('$'):
        if message.content == '$spam':
            pass
        print(message.content)


client.run("add token")
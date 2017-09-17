import Discord 
import asyncio
import random
import pickle
import os

client -Discord.client()

client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

@client.event
async def on_message(message):
    if message.content.startswith('!isYouCool')
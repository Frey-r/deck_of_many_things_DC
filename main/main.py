import discord
from discord_easy_commands import EasyBot
import random
from dotenv import load_dotenv
import os

import deck

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = EasyBot()

@bot.event
async def on_message(message):
    if message.content == '!robar':
        print("Channel: {0.channel} | User {0.author} : {0.content}".format(message))
        carta_aleatoria = deck.deckear()
        await message.channel.send("{0.author} ".format(message)+carta_aleatoria)

    if message.content == '!descarte':
        carta_aleatoria = deck.discardDeck()
        await message.channel.send("{0.author} ".format(message)+carta_aleatoria)

bot.run(TOKEN)
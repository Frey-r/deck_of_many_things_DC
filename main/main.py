import discord
from discord_easy_commands import EasyBot
import random
from dotenv import load_dotenv
import os

import deck

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
IMG_RUTE =os.getenv('IMG_RUTE')
bot = EasyBot()

@bot.event
async def on_message(message):
    if message.content == '!robar':
        carta_aleatoria = deck.deckear()
        respuesta = f"{message.author.mention}, tu carta es:\n{carta_aleatoria}"
        if not carta_aleatoria:
            respuesta = f"{message.author.mention} No quedan cartas en el mazo..."
        else:
            with open(f"{IMG_RUTE}{carta_aleatoria.lower()}.jpg", "rb") as file:
                await message.channel.send(respuesta, file=discord.File(file))

    if message.content == '!descarte':
        carta_aleatoria = deck.discardDeck()
        respuesta = f"{message.author.mention}, tu carta es:\n{carta_aleatoria}"
        if not carta_aleatoria:
            respuesta = f"{message.author.mention} No hay cartas descartadas..."
            await message.channel.send(respuesta)
        else:
            with open(f"{IMG_RUTE}{carta_aleatoria.lower()}.jpg", "rb") as file:
                await message.channel.send(respuesta, file=discord.File(file))

bot.run(TOKEN)
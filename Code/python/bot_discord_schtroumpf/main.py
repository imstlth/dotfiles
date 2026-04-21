# TODO
# - dès que quelqu'un mentionne le bot, il dit genre bonjour
# - dès que quelqu'un dit "quoi ?" (peu importe les maj), le bot s'incruste dans la discussion et dit "Quoicoubeh"
# - un truc d'astrologie
# ✅des photos de chat et de chien
# ✅des memes aléatoires/quotidien/trending/etc... juste quotidien pour l'instant
# - générateur de memes
# - https://docs.api.amethyste.moe/api-reference/generate
# - vidéo wa phoque

# TOKEN API

# Pour les commandes slash :
# https://stackoverflow.com/questions/71165431/how-do-i-make-a-working-slash-command-in-discord-py

import discord
# C'est déconseillé d'utiliser ce module pour un bot discord mais honnêtement osef
import requests
import bs4
from discord.ext import commands
import random

BOT_TOKEN = #perdu à jamais

# Les constantes en majuscule au début comme ça c'est plus simple
SERVER_ID = 784861431224205355
SERVER_OBJECT = discord.Object(id=SERVER_ID)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
bot = commands.Bot(command_prefix="!", intents=intents)
@tree.command(
    name="chachat",
    description="Tu veux un miaou ?",
    guild=SERVER_OBJECT
    )
async def photo_de_chat(interaction):
    requete = requests.get("https://api.thecatapi.com/v1/images/search")
    lien = requete.json()[0]["url"]
    requete.close()
    await interaction.response.send_message(lien)

@tree.command(
    name="doggo",
    description="Tu veux un waouf ?",
    guild=SERVER_OBJECT
    )

@client.event
async def on_message(message):
    if message.author != client.user and "quoi" in message.content.lower():
        await message.channel.send("Quoicoubeh !")

async def photo_de_chien(interaction):
    requete = requests.get("https://api.thedogapi.com/v1/images/search")
    lien = requete.json()[0]["url"]
    requete.close()
    await interaction.response.send_message(lien)

@tree.command(
    name="meme",
    description="Recupère un bon meme sur Reddit (1 à 2 x par jour)",
    guild=SERVER_OBJECT
    )
async def meme(interaction):
    reddit_req = requests.get("https://www.reddit.com/r/memes/hot/")
    soup = bs4.BeautifulSoup(reddit_req.content)
    lien = soup.find(id="post-image")["srcset"].split()[-2]
    await interaction.response.send_message(lien)


# JSP pk mais il a pas les perms pour lire les messages normaux des gens
# donc on peut que lui faire une commande quoicoubeh
# au lieu qu'il le dise dès que quelque le dit
@tree.command(
    name="quoi",
    description="Vasy ose",
    guild=SERVER_OBJECT
    )
async def quoi(interaction):
    await interaction.response.send_message("Quoicoubeh !")

@client.event
async def on_ready():
    await tree.sync(guild=SERVER_OBJECT)
    # À chaque fois qu'on le démarre, il y a 1/5 chances qu'il envoie la vidéo wa
    if random.random() < 0.2:
        print("vidéo envoyée")
        await client.get_channel(1069322866564272239).send("https://youtu.be/LZ5gyhj5qeE")
    print("ZUUMBA !!")

client.run(BOT_TOKEN)

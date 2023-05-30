import asyncio
import os
import random
from dotenv import load_dotenv
import discord
from discord.ext import commands
import main
from utils.Utils import send

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")

channels = [1113012348236603472]
json = "I used the json to destroy the json"
cooldown = False


@client.event
async def on_ready():
    await send(json)
    for channel in channels:
        await send("trash talked")
        await client.get_channel(channel).send("Get ready to be destroyed, trash.")


@client.event
async def on_message(message):
    channel_id = message.channel.id

    if message.author.bot:
        await send("filthy bot")
        return

    if channel_id not in channels:
        return

    if message.contentlower() == "ping" and main.cooldown:
        await send("too soon")
        await client.get_channel(channel_id).send("it is not time yet you filthy animal")

    if message.content.lower() == "pong":
        await send("wrong input")
        await client.get_channel(channel_id).send("that is my line you absolute buffoon")

    if message.content.lower() == "ping" and main.cooldown is False:
        main.cooldown = True
        await send("ping initiated")
        await response(channel_id)


async def response(channel_id):
    timer = random.randint(5, 15)
    await asyncio.sleep(timer)
    await send("ponging")
    await client.get_channel(channel_id).send("pong")
    main.cooldown = False

    await asyncio.sleep(5)

    if main.cooldown is False:
        await send("lost to a bot")
        await client.get_channel(channel_id).send("get absolutely owned trash, u lost against a bot smh")


load_dotenv()
client.run(os.getenv("TOKEN"))

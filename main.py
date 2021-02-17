import platform
import random
import discord
import discord.utils
import requests
import urllib
import secrets
import asyncio
import re
import time
import os
import aiofiles
import dataclasses
import math
import dbm
import discord.utils
import datetime
import discord
import asyncio
import random
import re
import requests
import base64
import os
import time
import numbers
import youtube_dl
import io
import json
import math
import sys
import json
import aiohttp
import http
from datetime import date, datetime, timedelta
from certifi.__main__ import args
from discord.ext import commands
from discord import User
from discord.ext.commands import Bot, guild_only
from discord.ext import commands
from discord.voice_client import VoiceClient
from asyncio import sleep
from datetime import datetime, timedelta
from re import search
from typing import Optional
from discord import Embed, Member, NotFound, Object
from discord.utils import find
from io import BytesIO
from discord.ext.commands import Cog, Greedy, Converter
from discord.ext.commands import CheckFailure, BadArgument
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord import abc
from discord import Intents
from replit import db
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=['e!', 'E!'], case_insensitive=True, intents=intents)
client.warnings = {}
client.remove_command("help")


async def ch_pr():
    await client.wait_until_ready()

    statuses = [
        f"on {len(client.guilds)} servers | e!help | Made by Runo#0001 and pip#5672",
        f"on {len(client.guilds)} servers. | e!help | Made by Runo#0001 and pip#5672"
    ]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(10)



@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.bot == False:
        for x in message.mentions:
            if x.id == 803358415953854524:
                await message.channel.send('My prefix is **e!**')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# ERROR HANDLING


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("> No permissions.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("> Missing arguments.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("> Invalid command.")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("> User not found.")
    elif isinstance(error, commands.ChannelNotFound):
        await ctx.send("> Channel not found.")
    elif isinstance(error, commands.RoleNotFound):
        await ctx.send("> Role not found.")
    elif isinstance(error, commands.MessageNotFound):
        await ctx.send("> Message not found.")
    elif isinstance(error, commands.TooManyArguments):
        await ctx.send("> Too many arguments.")
    else:
        raise error


# SECRET


@client.command()
async def secret(ctx):
    await ctx.send(
        "How did you find out about this? You just won a reward, DM Runo#8422")


# OTHER2


@client.command()
async def flushed(ctx):
    await ctx.send(":flushed: :flushed: :flushed:")


@client.command()
async def cry(ctx):
    await ctx.send(
        ":sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob: :sob:"
    )


@client.command()
async def heart(ctx):
    await ctx.send(
        ":heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: "
    )




# MUSIC TEST


client.loop.create_task(ch_pr())

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("ODAzMzU4NDE1OTUzODU0NTI0.YA8n1A.Gwf3zkNpCET-Oy-IHhcw1zSzAgk")
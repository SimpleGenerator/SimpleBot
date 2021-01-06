import discord
import random
import asyncio
import functools
import discord.utils
import sys
import os
from discord.ext.commands import when_mentioned
import time
import datetime
import json
from discord import Member
import urllib.request
from pyfiglet import Figlet
from itertools import cycle
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import enum
import time
import pymysql
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from discord import Message, Guild, TextChannel
import schedule

intents = discord.Intents().all()
client = commands.Bot(command_prefix="/", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print('Bot is online.')
    await client.change_presence(activity=discord.Game('SimpleAlts - Beta'))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(
            title=":x: Error",
            description="/gen __``service``__" "\n" "\n" + "# **__Help__**" "\n" + "```Maybe the service you choosed is currently not in stock or you typed it false. Please make sure that you write the service always small.```" "\n" "\n" + "# **__How to use__**" "\n" + f"Example: /gen ~~Minecraft~~ | /gen minecraft", color=0xe74c3c
        )
        await ctx.send(embed=embed)
    else:
        pass

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title=":x: Error",
                description="/gen __``service``__" "\n" "\n" + "# **__Generator__**" "\n" + "```minecraft, origin, roblox, hulu, disney, email, crunchyroll, nordvpn, spotify, stock```", color=0xe74c3c
            )
            await ctx.send(embed=embed)
        else:
            pass

            if isinstance(error, commands.MissingRole):
                embed = discord.Embed(
                    title=":x: Error",
                    description=f"{ctx.message.author.mention} you __CANT__ use that!", color=0xe74c3c
                )
                await ctx.send(embed=embed)
            else:
                pass

@commands.has_role("OWNER")
@client.command()
async def enable(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(
        title=":white_check_mark: SimpleAlts",
        description=f"{ctx.message.author.mention} toggled {extension} on!", color=0x3498db
    )
    await ctx.send(embed=embed)

@commands.has_role("OWNER")
@client.command()
async def disable(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(
        title=":white_check_mark: SimpleAlts",
        description=f"{ctx.message.author.mention} toggled {extension} off!", color=0x3498db
    )
    await ctx.send(embed=embed)

@commands.has_role("OWNER")
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(
        title=":white_check_mark: SimpleAlts",
        description=f"{ctx.message.author.mention} Successfully reloaded {extension}", color=0x3498db
    )
    await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run("Nzk0MTkzODMzMjY0OTM5MDA4.X-3QpQ.oZt4X_l5Zcd9TdNegnL524NJ3KQ")
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

client = discord.Client()

class Welcome(commands.Cog):

    def __init__(self, client):
        self.client = client
        self._last_member = None


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(
                description="Welcome {0.mention} to SimpleAlts".format(member), color=0x00a8ff
            )
            await channel.send(embed=embed)            


def setup(client):
    client.add_cog(Welcome(client))
import discord
from discord.ext import commands
import pymysql
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import asyncio
import time

class Generator(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands

    @commands.has_role("Member")
    @commands.command()
    async def stock(self, ctx):
        connection = pymysql.connect(
            host='82.165.242.22',
            database='demo',
            user='admin',
            password='Kleinemaus1!')
    
        sql_select_Query = "select * from spotify"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        spstock = cursor.rowcount
    
        sql_select_Query = "select * from minecraft"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        mcstock = cursor.rowcount
    
        sql_select_Query = "select * from origin"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        orstock = cursor.rowcount
    
        sql_select_Query = "select * from hulu"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        hustock = cursor.rowcount
    
        sql_select_Query = "select * from email"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        fastock = cursor.rowcount
    
        sql_select_Query = "select * from roblox"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        rbstock = cursor.rowcount
    
        sql_select_Query = "select * from disney"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        dsstock = cursor.rowcount
    
        sql_select_Query = "select * from nordvpn"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        nvstock = cursor.rowcount
    
        sql_select_Query = "select * from crunchyroll"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.rowcount
    
        crstock = cursor.rowcount
    
        embed = discord.Embed(title="Bot prefix = /", color=0x00a8ff)
        embed.add_field(name="Spotify", value=f"‍{spstock}", inline=False)
        embed.add_field(name="Minecraft", value=f"‍{mcstock}", inline=False)
        embed.add_field(name="Origin", value=f"‍{orstock}", inline=False)
        embed.add_field(name="Roblox", value=f"‍{rbstock}", inline=False)
        embed.add_field(name="Hulu", value=f"‍{hustock}", inline=False)
        embed.add_field(name="Disney", value=f"‍{dsstock}", inline=False)
        embed.add_field(name="Email", value=f"‍{fastock}", inline=False)
        embed.add_field(name="NordVPN", value=f"‍{nvstock}", inline=False)
        embed.add_field(name="Crunchyroll", value=f"‍{crstock}", inline=False)
        await ctx.send(embed=embed)


    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.has_role("Member")
    @commands.command(aliases=["generate"])
    async def gen(self, ctx, *, service):

        connection = pymysql.connect(
            host='82.165.242.22',
            database='demo',
            user='admin',
            password='Kleinemaus1!')
    
        sql_select_Query = f"SELECT * FROM {service} ORDER BY RAND() LIMIT 1;"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        for row in records:
            accounts = row[1]

        embed = discord.Embed(
            title=":white_check_mark: Account Generator",
            description=f"# **__{service}__**" "\n" + "*just copy the following link and paste it in your browser.*" "\n" + f"```{accounts}```" "\n" "\n" "# **__Help__**" "\n" + "```Hello, first thank you for using SimpleAlts 💖 We know 'ShrinkUrl' is kinda weird and buggy so we provide 24/7 Support on our Discord server. Just check out the #tickets channel and react to the message to create a ticket then just wait till an staff contact you! We will change back to Linkvertise when they finally block bypasser etc.```" "\n" "\n" + " # **__Support__** ```https://paypal.me/simplemain```", color=0x3498db
        )
        await ctx.author.send(embed=embed)
        
        embed = discord.Embed(
            title=f":white_check_mark: Successfully generated!",
            description=f"{ctx.message.author.mention} check your dm´s.", color=0x3498db
        )
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Generator(client))
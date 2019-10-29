import discord
import random
import asyncio
import functools
import sys
import os
from discord.ext.commands import when_mentioned
import time as tm
import colorama
from discord import Member
from colorama import Fore, Back, Style
colorama.init()
import urllib.request
from pyfiglet import Figlet
from itertools import cycle
from discord.utils import get
from discord.ext import commands, tasks
from terminaltables import DoubleTable
from terminaltables import SingleTable
from discord.ext.commands import has_permissions, MissingPermissions


table_data = [
    ['Name >    ', 'SimpleGenerator'],
    ['ID   >    ', '629656985213861899'],
]



client = commands.Bot(command_prefix = '>')
client.remove_command("help")
status = cycle(['SimpleGenerator', '>spotify', '>hulu'])



@client.event
async def on_ready():
    change_status.start()

    title= '\033[32m' + 'By yCode & BLZKRG' + '\033[39m'
    table = DoubleTable(table_data, title)
    print (table.table)
    print(Style.RESET_ALL)



@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
    channel = ctx.message.channel
    channel = client.get_channel(id=630363228718891038)
    await ctx.channel.send("Moin servus moin")



@client.command()
async def antiafk():
    response = random.choice([">spotify", ">hulu", ">help"])
    await bot.say(response)
    await asyncio.sleep(1)


@commands.cooldown(1, 120, commands.BucketType.user)

@client.command()
async def hulu(ctx):
    await ctx.channel.purge(limit=1)
    author  = ctx.message.author
    accounts = urllib.request.urlopen('https://pastebin.com/raw/jxmgspFt').read().splitlines()
    accounts = random.choice(accounts)
    accounts=str(accounts,'utf-8')
    embed = discord.Embed(
        title = "SimpleGenerator",
        description = "free account generator",
        colour = discord.Colour.green()
    )

    embed.set_footer(text=author)
    embed.add_field(name="Account", value=accounts, inline=False)
    embed.add_field(name="----SIMPLE----", value=">--------------<", inline=False)
    embed.add_field(name="Developer", value="Simple#1548", inline=False)
    embed.add_field(name="Link:", value="https://www.youtube.com/channel/UCDtcgX8sCmNS8_CKeJJpnzw?view_as=subscriber", inline=False)
    await ctx.author.send(embed=embed)

    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleGenerator",
        description = "free account generator",
        colour = discord.Colour.green()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name="Hulu generated check DMs", value=author, inline=False)
    embed.add_field(name="Cooldown", value="please wait 2m", inline=False)
    await ctx.send(embed=embed)
    table_instance = SingleTable([['\033[31m' + "[>Hulu]" +'\033[39m' " command used by", author, "account he got:", accounts]], 'Acccount')
    print(table_instance.table)



@hulu.error
async def hulu_error(ctx, error):
    author = ctx.message.author
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(channel, "Please wait 2m")
        print(author, "overtyped")







@commands.cooldown(1, 120, commands.BucketType.user)

@client.command()
async def spotify(ctx):
    await ctx.channel.purge(limit=1)
    author  = ctx.message.author
    accounts = urllib.request.urlopen('https://pastebin.com/raw/jxmgspFt').read().splitlines()
    accounts = random.choice(accounts)
    accounts=str(accounts,'utf-8')
    embed = discord.Embed(
        title = "SimpleGenerator",
        description = "free account generator",
        colour = discord.Colour.green()
    )

    embed.set_footer(text=author)
    embed.add_field(name="Account", value=accounts, inline=False)
    embed.add_field(name="----SIMPLE----", value=">--------------<", inline=False)
    embed.add_field(name="Developer", value="Simple#1548", inline=False)
    embed.add_field(name="Link:", value="https://www.youtube.com/channel/UCDtcgX8sCmNS8_CKeJJpnzw?view_as=subscriber", inline=False)
    await ctx.author.send(embed=embed)

    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleGenerator",
        description = "free account generator",
        colour = discord.Colour.green()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name="Spotify generated check DMs", value=author, inline=False)
    embed.add_field(name="Command Cooldown", value="please wait 2m", inline=False)
    await ctx.send(embed=embed)
    table_instance = SingleTable([['\033[31m' + "[>spotify]" +'\033[39m' " command used by", author, "account he got:", accounts]], 'Acccount')
    print(table_instance.table)



@spotify.error
async def spotify_error(ctx, error):
    author = ctx.message.author
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(channel, "Please wait 2m")
        print(author, "overtyped")




@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)
    channel = discord.utils.get(member.guild.channels, name="general")
    embed = discord.Embed(
        title = "SimpleModerator",
        colour = discord.Colour.blue()
    )

    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name=member.display_name, value="Welcome on our server :)", inline=False)
    await channel.send(embed=embed)







@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    embed = discord.Embed(
        title = "SimpleModerator",
        colour = discord.Colour.blue()
    )

    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name=member.display_name, value="left our server :(", inline=False)
    await channel.send(embed=embed)



@commands.cooldown(1, 10, commands.BucketType.user)

@client.command()
async def dev(ctx):
    await ctx.author.send("https://www.youtube.com/channel/UCDtcgX8sCmNS8_CKeJJpnzw?view_as=subscriber")

@commands.cooldown(1, 10, commands.BucketType.user)

@client.command()
async def invite(ctx):
    await ctx.author.send("Soon...")



@commands.cooldown(1, 10, commands.BucketType.user)

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]
    author = ctx.message.author
    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleModerator",
        description = "free moderator bot",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name="Name", value=member.display_name)
    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Created at", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name=f"Roles", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role", value=member.top_role.mention)
    embed.add_field(name="Avatar", value=f"The avatar of {member.name} is: {member.avatar_url_as(static_format='png')}")
    embed.add_field(name="Bot", value=member.bot)
    await channel.send(embed=embed)

@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("> >userinfo @member")





@commands.cooldown(1, 10, commands.BucketType.user)

@client.command()
@has_permissions(kick_members=True, ban_members=True)
async def help(ctx):

    author = ctx.message.author
    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleModerator",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name=">spotify", value="get a spotify account", inline=False)
    embed.add_field(name=">hulu", value="get a hulu account", inline=False)
    embed.add_field(name=">mute @member", value="mute a user", inline=False)
    embed.add_field(name=">kick @member", value="kick a user", inline=False)
    embed.add_field(name=">ban @member", value="ban a user", inline=False)
    embed.add_field(name=">userinfo @member", value="see informations about a member", inline=False)
    embed.add_field(name=">report @member reason", value="see informations about a member", inline=False)
    embed.add_field(name=">warn @member", value="warn members", inline=False)
    embed.add_field(name=">clear amount", value="clear messages", inline=False)
    embed.add_field(name=">purge", value="purge channel", inline=False)
    embed.add_field(name=">ping", value="see your ping", inline=False)
    embed.add_field(name=">dev", value="developers youtube channel", inline=False)
    embed.add_field(name=">invite", value="give u a bot invite link", inline=False)
    embed.add_field(name="join message", value="will send in the general channel", inline=False)
    embed.add_field(name="leave message", value="will send in the general channel", inline=False)
    await channel.send(embed=embed)

@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("ERROR: Please contact a Moderator")


@commands.cooldown(1, 10, commands.BucketType.user)

@client.command()
async def gen(ctx):

    author = ctx.message.author
    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleModerator",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name=">spotify", value="get a spotify account", inline=False)
    embed.add_field(name=">hulu", value="get a hulu account", inline=False)
    await channel.send(embed=embed)

@gen.error
async def gen_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("ERROR: Please contact a Moderator")



@client.command()
@has_permissions(kick_members=True, ban_members=True)
async def ban(ctx, user:discord.Member, *, reason=None):
        if reason is None:
            await ctx.guild.ban(user=user, reason='None')
            await ctx.send(f'> {user} has been banned.')
        else:
            await ctx.guild.ban(user=user, reason=reason)
            await ctx.send(f'> {user} has been banned.')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('> You do not have permissions to use this command.')






@client.command()
@has_permissions(kick_members=True, ban_members=True)
async def kick(ctx, user:discord.Member, *, reason=None):
        if reason is None:
            await ctx.guild.kick(user=user, reason='None')
            await ctx.send(f'> {user} has been kicked.')
        else:
            await ctx.guild.kick(user=user, reason=reason)
            await ctx.send(f'> {user} has been kicked.')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('> You do not have permissions to use this command.')






@client.command(pass_context=True)
@has_permissions(kick_members=True, ban_members=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    if not member:
        await ctx.send("> You cant use that!")
        return
    author = ctx.message.author
    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleModerator",
        colour = discord.Colour.red()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name="Discord member", value=f"{member.mention}", inline=False)
    embed.add_field(name="got warned by", value=f"{author}", inline=False)
    embed.add_field(name="reason", value=f"{reason}", inline=False)
    await channel.send(embed=embed)

@warn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("> You cant use that!")






@commands.cooldown(1, 10, commands.BucketType.user)

@client.command(pass_context=True)
async def report(ctx, member : discord.Member, *, reason=None):
    if not member:
        await ctx.send("ERROR: >report @member reason")
        return
    author = ctx.message.author
    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleModerator",
        colour = discord.Colour.red()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name="Discord member", value=f"{member.mention}", inline=False)
    embed.add_field(name="got reported by", value=f"{author}", inline=False)
    embed.add_field(name="reason", value=f"{reason}", inline=False)
    await channel.send(embed=embed)

@report.error
async def report_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("> >report @member reason")





@client.command()
@has_permissions(kick_members=True, ban_members=True)
async def mute(ctx, member : discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send(">mute @member reason")
        return
    await member.add_roles(role)

    author = ctx.message.author
    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleModerator",
        colour = discord.Colour.red()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name="Discord member", value=f"{member.mention}", inline=False)
    embed.add_field(name="got muted by", value=f"{author}", inline=False)
    embed.add_field(name="reason", value=f"{reason}", inline=False)
    await channel.send(embed=embed)

@mute.error
async def error_mute(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("> You cant use that!")

@client.command()
@has_permissions(kick_members=True, ban_members=True)
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send(">unmute @member")
        return
    await member.remove_roles(role)

    author = ctx.message.author
    channel = ctx.message.channel
    embed = discord.Embed(
        title = "SimpleModerator",
        colour = discord.Colour.red()
    )

    embed.set_footer(text=author)
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/1iiKTlNl6wzC06SbhBW-c1cBkYzNRIQM3gcFZQ832IKYgCi-oqYz9niZr3uVO633Jvnb1AiexZVryA=w176-h176-n-o-rw")
    embed.add_field(name="Discord member", value=f"{member.mention}", inline=False)
    embed.add_field(name="got unmuted by", value=f"{author}", inline=False)
    await channel.send(embed=embed)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("> You cant use that!")


@commands.cooldown(1, 10, commands.BucketType.user)
@client.command()
@has_permissions(kick_members=True, ban_members=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)



@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("> You cant use that!")




@commands.cooldown(1, 10, commands.BucketType.user)
@client.command()
@has_permissions(kick_members=True, ban_members=True)
async def purge(ctx, amount=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    await ctx.channel.purge(limit=amount)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("> You cant use that!")


@client.command()
async def ping(ctx):
    await ctx.send(f'> Ping -> {round(client.latency * 10000)}')

client.run("NjM2NjIzMjc4NDk2MTUzNjIw.XbCTvg.dldyG4vqcOQNkcjFobZBaKUTmEQ")

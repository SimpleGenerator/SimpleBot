import discord
from discord.ext import commands
import time
import datetime

class Cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.has_role("Member")
    @commands.command(aliases=["Help", "HELP", "hilfe", "Hilfe", "HILFE", "commands", "Commands", "COMMANDS", "cmd", "CMD", "Cmd", "Command", "command", "cOMMAND", "Minecraft", "Origin", "Roblox", "Hulu", "Disney", "Email", "Crunchyroll", "Nordvpn", "Spotify", "minecraft", "origin", "roblox", "hulu", "disney", "email", "crunchyroll", "nordvpn", "spotify"])
    async def help(self, ctx):
        embed = discord.Embed(
            title=":person_raising_hand: Help Command",
            description="# **__Generator__** | */gen __service__*" "\n" + "```minecraft, origin, roblox, hulu, disney, email, crunchyroll, nordvpn, spotify```" "\n" "\n" + 
            "# **__CONFIG__** | *__/enable__* | *__/disable__*" "\n" + "```generator, cmd, welcome```" "\n" "\n" + 
            "# **__MISC__** | *__/command__*" "\n" + "```invite, serverinfo, help, stock```" "\n" "\n" + f"{datetime.datetime.now()}", color=0x3498db
        )
        await ctx.send(embed=embed)

    @commands.has_role("Member")
    @commands.command(aliases=["create_invite", "Invite", "INVITE", "createinvite", "iNVITE"])
    async def invite(self, ctx):
        embed=discord.Embed(description=f'{(await ctx.channel.create_invite()).url}', color=0xff0000)
        await ctx.send(embed=embed)
        
    @commands.has_role("Member")
    @commands.command(aliases=["vERIFY", "Verify"])
    async def verify(self, ctx):
        embed = discord.Embed(title="SimpleAlts", url="http://simplealts.eu/", color=0x00a8ff)
        embed.add_field(name="Username:", value=f"{ctx.message.author.mention}", inline=True)
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1175689543271571456/Qk9MQmac.png")
        embed.add_field(name="Role:", value="Verified", inline=True)
        await ctx.author.send(embed=embed)
        await ctx.message.author.add_roles(discord.utils.get(ctx.message.author.guild.roles, name="Member"))
        
    @commands.has_role("Member")
    @commands.command(aliases=["Invites", "iNVITES"])
    async def invites(self, ctx, user = None):
        if user == None:
          totalInvites = 0
          for i in await ctx.guild.invites():
              if i.inviter == ctx.author:
                  totalInvites += i.uses
          await ctx.send(f"You've invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server! *__BETA__*")
        else:
          totalInvites = 0
          for i in await ctx.guild.invites():
             member = ctx.message.guild.get_member_named(user)
             if i.inviter == member:
               totalInvites += i.uses
          await ctx.send(f"{member} has invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server!")

    @commands.has_role("Member")
    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")

    @commands.has_role("Member")
    @commands.command(aliases=["ServerInfo", "Serverinfo", "SERVERINFO", "sERVERINFO"])
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title="SimpleBot",
            description=
            f"Total Member: `{len(ctx.guild.members)}`"
            "\n" + f"Total Roles: `{len(ctx.guild.roles)}`"
            "\n" + f"Total Emojis: `{len(ctx.guild.emojis)}`"
            "\n" + f"Total Categories: `{len(ctx.guild.categories)}`"
            "\n" + f"Total Channels: `{len(ctx.guild.channels)}`"
            "\n" + f"Total Text_Channels: `{len(ctx.guild.text_channels)}`"
            "\n" + f"Total Voice_Channels: `{len(ctx.guild.voice_channels)}`", color=0x00a8ff)
        await ctx.send(embed=embed)

    @commands.has_role("Moderator")
    @commands.command()
    async def say(self, ctx, *, arg):
        await ctx.send(arg)

    @commands.has_role("Moderator")
    @commands.command()
    async def embed(self, ctx, arg):
        embed = discord.Embed(
            title="SimpleAlts",
            description=arg, color=0x00a8ff
        )
        await ctx.send(embed=embed)

    @commands.has_role("Moderator")
    @commands.command()
    async def purge(self, ctx):
        await ctx.channel.purge(limit=None)


    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        await self.client.get_channel(783276327293812747).send(f"{member.mention} got banned.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
       ment = member.mention
       await self.client.get_channel(783276327293812747).send(f"{ment} joined the server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        ment = member.mention
        await self.client.get_channel(783276327293812747).send(f"{ment} left the server")

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        await self.client.get_channel(783276327293812747).send(f"{member.mention} got unbanned")

        
def setup(client):
    client.add_cog(Cmd(client))
import discord
import asyncio


client = commands.Bot(command_prefix = '>')
client.remove_command("help")



@client.event
async def on_ready():
    print("ON")
    
 
@client.command()
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
    
client.run("NjM2NjIzMjc4NDk2MTUzNjIw.XbCTvg.dldyG4vqcOQNkcjFobZBaKUTmEQ")

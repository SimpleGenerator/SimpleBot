import discord
import asyncio


client = commands.Bot(command_prefix = '>')
client.remove_command("help")



@client.event
async def on_ready():
    print("ON")
    
 
@client.command()
async def hi(ctx):
    await ctx.send("Hello")
    
client.run("NjM2NjIzMjc4NDk2MTUzNjIw.XbCTvg.dldyG4vqcOQNkcjFobZBaKUTmEQ")

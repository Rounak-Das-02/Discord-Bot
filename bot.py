import discord
from discord.ext import commands
import os
import json

client = commands.Bot(command_prefix = ".")

# @client.command()
# async def load(ctx , extensions):
#     client.load_extensions(f"cogs.{extensions}")



# @client.command()
# async def unload(ctx , extensions):
#     client.unload_extension(f"cogs.{extensions}")



for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.event
async def on_command_error(ctx , error):
    if isinstance(error , commands.CommandNotFound):
        await ctx.send("Invalid Command")


f = open(r".\tokens\token.json", )
s = json.load(f)

client.run(s["Token"])

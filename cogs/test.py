import discord
from discord.ext import commands

class test(commands.Cog):

    def __init__(self , client):
        self.client = client


    @commands.command()
    async def tt(self , ctx):
        await ctx.send("test successful")

    

def setup(client):
    client.add_cog(test(client))


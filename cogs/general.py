import discord
from discord.ext import commands


class general(commands.Cog):

    def __init__(self, client):
        self.client = client 



    @commands.command(name = "ping")
    # @commands.has_permissions(manage_messages = True)                     # A check
    async def ping(self,ctx):
        await ctx.channel.send(f"Hi {ctx.author.mention} , I am here dude.")


    @commands.command(name = "owner")
    async def get_owner(self , ctx):
        await ctx.channel.send(f"{self.client.appInfo.owner.mention} is my owner! ")



    ## Make APIs in weathermap , and news.
       


def setup(client):
    client.add_cog(general(client))
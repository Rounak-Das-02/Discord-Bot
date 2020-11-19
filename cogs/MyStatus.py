import discord 
from discord.ext import commands 

class MyStatus(commands.Cog):

    def __init__(self , client):
        self.client = client

    @commands.command(name = "offline")
    @commands.is_owner()
    async def go_offline(self , ctx):
        await ctx.channel.send("Going Offline")
        await self.client.change_presence(status = discord.Status.offline)
        await self.client.logout()

    @commands.command(name = "invisible")
    @commands.is_owner()
    async def go_invisible(self , ctx):
        await ctx.channel.send("Going invisible")
        await self.client.change_presence(status = discord.Status.invisible)

    @commands.command(name = "online")
    @commands.is_owner()
    async def go_online(self , ctx):
        await ctx.channel.send("I am now online")
        await self.client.change_presence(status = discord.Status.online)


    @go_online.error
    async def on(self , ctx , error):
        if isinstance(error , commands.CommandError):
            await ctx.channel.send("This function is only for the owner .. type .owner to find out the owner")

    @go_offline.error
    async def off(self , ctx , error):
        if isinstance(error , commands.CommandError):
            await ctx.channel.send("This function is only for the owner .. type .owner to find out the owner")




def setup(client):
    client.add_cog(MyStatus(client))
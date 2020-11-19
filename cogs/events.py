import discord
from discord.ext import commands

class events(commands.Cog):

    def __init__(self,client):
        self.client = client

    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status = discord.Status.online , activity = discord.Game("In dev mode|.help"))
        print("Bot is online")


    #####################PING##################################

    #Command
    @commands.command()
    async def ping(self , ctx):
        await ctx.send(f"Ping : {round(self.client.latency*1000)}ms")

    ###########################################################



    ###############Clear Command ##############################
    @commands.command()
    async def clear(self , ctx , amount = 5):
        await ctx.channel.purge(limit = amount)

    @clear.error
    async def clear_error(self , ctx , error):
        if isinstance(error , commands.CommandError):
            await ctx.channel.send("Command Error , Example : \n .clear 5")

    ###########################################################



    @commands.Cog.listener()
    async def on_message(self , message):
        msg = message.content.lower()
        if not message.author.bot and message.author!=self.client.user:

                if ((msg.startswith('hi') or msg.startswith('hey') or msg.startswith('sup') or msg.startswith("hello"))):
                    await message.channel.send("Sup {}".format(message.author.mention)) #Direct message.channel.send  -> Infinity loop
                    
                    
                elif ((msg.startswith('gn') or 'good night' in msg or "goodnight" in msg)):
                    await message.channel.send(f"Good night {message.author.mention} \n Sweet Dreams")
                    
                    
                elif ('bye' in msg):
                    await message.channel.send('Goodbye {}'.format(message.author.mention))
                
            
            

def setup(client):
    client.add_cog(events(client))

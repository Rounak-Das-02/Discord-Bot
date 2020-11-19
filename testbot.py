import discord
from discord.ext import commands
import json

client = discord.Client()
bot = commands.Bot(command_prefix = ".")


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.event
async def on_member_join(member):
    print(f"{member} has joined the server")

@bot.event
async def on_member_remove(member):
    print(f"{member} has left the server")  


@bot.command()
async def ping(ctx):
    await ctx.send(f"ping : {round(bot.latency)*1000}ms ")


@bot.command(aliases = ["8ball" , "test"])
async def _8ball(ctx , * , question ):
    await ctx.send(f"Question : {question} \n Answer : It is working")

@bot.command()
async def clear(ctx , amount = 7):
    await ctx.channel.purge(limit = amount)

@bot.command()
async def kick(ctx , member : discord.Member , * , reason = None):
    await member.kick(reason = reason)

@bot.command()
async def ban(ctx , member : discord.Member , * , reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.mention}")

@bot.command()
async def unban(ctx , * , member):
    banned_users = await ctx.guild.bans()
    member_name , member_discriminator = member.split("#")

    for ban_entry in banned_users:

        if(ban_entry.user.name ,ban_entry.user.discriminator) == (member_name , member_discriminator):
            await ctx.guild.unban(ban_entry.user)
            await ctx.send(f"Unbanned {ban_entry.user.name}#{ban_entry.user.discriminator}")
            return


f = open(r"E:\discord bot\token.json", )
s = json.load(f)

bot.run(s["Token"])

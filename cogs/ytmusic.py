import discord 
from discord.ext import commands
import requests
import urllib.request
import re
import youtube_dl
from discord import FFmpegPCMAudio
import asyncio

class music(commands.Cog):
    
    def __init__(self , client):
        self.client = client
    

    def check_queue():
        pass
    

    def my_after(error):
        coro = self.client.channel.send('Song is done!')
        fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
        try:
            fut.result()
        except:
            # an error happened sending the message
            pass
    
    @commands.command(name = "play")        
    async def yt_music(self , ctx , * , search):        ##For playing from youtube

        search = search.replace(" " , "+")
        html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search}")
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        url = "https://www.youtube.com/watch?v=" + video_ids[0]
        await ctx.channel.send(f"{url}")
        channel = ctx.message.author.voice.channel


        vc = await channel.connect()

        try:
            ydl_opts = {'format': 'bestaudio'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                ##print("Duration in seconds : {} Likes : {} Dislikes : {} Title : {}".format(info["duration"] , info["like_count"] , info["dislike_count"] , info["title"]))
            playurl = info['formats'][0]['url']
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            source = discord.FFmpegPCMAudio(playurl , **FFMPEG_OPTIONS)
            vc.play(source , after = lambda e : print("Done playing" , e))
            await ctx.channel.send("Playing now")
            await asyncio.sleep(info["duration"])
            await ctx.voice_client.disconnect()

        except Exception as e:
            await ctx.channel.send(f"{e}")
            await ctx.voice_client.disconnect()

    
    @commands.command()
    async def playmy(self ,ctx ,  * , path):        #for playing from the local computer
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        try : 
            source = discord.FFmpegPCMAudio(path)   ##provide the file path in your local computer
            # ctx.voice_client.play(source)
            vc.play(source , after = lambda e : print("Done playing" , e))
            await ctx.channel.send("Playing now")
            await ctx.voice_client.disconnect()

        except Exception as e:
            await ctx.channel.send(f"Error : {e}")

    @commands.command()
    async def pause(self , ctx):
        ctx.voice_client.pause()
        await ctx.channel.send("paused")
        

    @commands.command()
    async def pause(self , ctx):
        ctx.voice_client.pause()
        await ctx.channel.send("paused")

    @commands.command()
    async def stop(self , ctx):
        ctx.voice_client.stop()
        await ctx.channel.send("stopped")

    @commands.command()
    async def resume(self , ctx):
        ctx.voice_client.resume()
        await ctx.channel.send("resumed")

    @commands.command(name = "leave")
    async def leave(self , ctx):
        await ctx.voice_client.disconnect()
        await ctx.channel.send("disconnected")


def setup(client):
    client.add_cog(music(client))

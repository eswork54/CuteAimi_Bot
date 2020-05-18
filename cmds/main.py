import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def hinow(self, ctx):
        await ctx.send(f'{datetime.datetime.now()}')

    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="Cute_aimi", url="https://www.instagram.com/my_name_is_aimi/", description="cutecute", color=0xf93ece,
        timestamp= datetime.datetime.utcnow())
        embed.set_author(name="Eason", url="https://medium.com/@eswork54", icon_url="https://i.imgur.com/0OvGcGt.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/0OvGcGt.jpg")
        embed.add_field(name="Aimi", value="my_waifu", inline=True)
        embed.add_field(name="Nickname", value="aimiaiai", inline=True)
        embed.set_footer(text="discord bot")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)

def setup(bot):
    bot.add_cog(Main(bot))
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

with open('eat.json','r', encoding='utf8') as efile:
    edata = json.load(efile)


class React(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eat(self,ctx):
        food_dict = edata
        all_data = []
        for v,w in list(food_dict.items()):
            temp = []
            for i in range(w):
                temp.append(v)
            all_data.extend(temp)
        random.shuffle(all_data)#打亂數據
        you_eat = random.choice(all_data)
        user_id = ctx.author.id
        await ctx.send(f'<@{user_id}> go to eat {you_eat}') 

    @commands.command()
    async def 圖片(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command()
    async def 網路圖片(self,ctx):
        random_pic = random.choice(jdata['web_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))

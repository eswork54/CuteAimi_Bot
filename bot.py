import discord
from discord.ext import commands
import json
import random

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

with open('eat.json','r', encoding='utf8') as efile:
    edata = json.load(efile)

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def eat(ctx):
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
    await ctx.send(f'<@{user_id}> go to eat{you_eat}') 


bot.run(jdata['TOKEN'])
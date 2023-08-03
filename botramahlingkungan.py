import discord
import os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



@bot.command()
async def idesampah(ctx):
    img_name = random.choice(os.listdir('sampah'))
    with open(f'gambar/{img_name}.', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('berikut saran kerajinan aku')  
    await ctx.send(file=picture)

    bot.run("")
    

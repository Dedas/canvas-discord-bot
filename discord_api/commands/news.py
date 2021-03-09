# Lists the 5 latest announcements

import discord
from discord.ext import commands
import os

from environs import load_dotenv

# TODO import data from database
news_list = ["Ann1", "Ann2", "Ann3", "Ann4", "Ann5", "Ann6", "Ann7"]

# TODO put in command_base?
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# TODO fallback ".", expose prefix variable in .env
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("{0.user} is online".format(client))


@client.command()
async def news(ctx):
    news = ""
    for i in news_list[0:5]:
        news = news + "\n" + i
    await ctx.channel.send(news)

client.run(TOKEN)
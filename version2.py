import discord
from discord.ext import commands

client = commands.Bot(command_prefix='~')

@client.event
async def on_ready():
    print('Bot is online')

@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    else:
        channel = message.channel
        author = message.author.mention
        await channel.send(f'{author}, please do not delete your messages.')

@client.slash_command()
async def ping(ctx):
    await ctx.send(f'Pong! My current ping is {round(client.latency * 1000)}ms')

TOKEN = 'your_token_here'
client.run(MTA4OTI3Mzc3ODIyOTQ4OTc5NQ.GT69Fw.yxpYvnyXJcrNAbjRieEEL_-NmdFj1Vq66acwTs)
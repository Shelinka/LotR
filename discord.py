import discord
from discord import app_commands
from discord.ext import commands

bot = comamnds.Bot(command_prefix="!", intents = discord.Intents.all())

#intents = discord.Intents(messages=True, guilds=True, members=True)
#bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


# Define a slash command for /ping
@client.command()
async def ping(ctx):
     await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')

@bot.event
async def on_message_delete(message):
    user = message.author
    await user.send(f"Heya! Please do not delte your messages in LFG channels. In case you delisted your group etc. you can always use the Edit function to let others know that your group is full. Thank you <3")

bot.run('YOUR_BOT_TOKEN')

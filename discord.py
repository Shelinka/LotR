import discord
from discord import app_commands
from discord.ext import commands

bot = comamnds.Bot(command_prefix="!", intents = discord.Intents.all())

#intents = discord.Intents(messages=True, guilds=True, members=True)
#bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message_delete(message):
    user = message.author
    await user.send(f"Heya! Please do not delte your messages in LFG channels. In case you delisted your group etc. you can always use the Edit function to let others know that your group is full. Thank you <3")

# Define a slash command for /ping
@bot.tree.command(name="ping", description="Get the current ping of the bot.")
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to milliseconds
    await ctx.send(f'Pong! Current ping is {latency:.2f} ms.')

bot.run('YOUR_BOT_TOKEN')

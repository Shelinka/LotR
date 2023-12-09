import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, members=True)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_message_delete(message):
    user = message.author
    await user.send(f"You deleted a message: '{message.content}'")

# Define a slash command for /ping
@bot.slash_command(name="ping", description="Get the current ping of the bot.")
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to milliseconds
    await ctx.send(f'Pong! Current ping is {latency:.2f} ms.')

bot.run('YOUR_BOT_TOKEN')

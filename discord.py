import discord
from discord.ext import commands

# Create an instance of the Intents class with all intents enabled
intents = discord.Intents.all()

# Create a new bot instance with the specified command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Event handler for when a message is deleted
@bot.event
async def on_message_delete(message):
    # Check if the deleted message matches the specified content
    if message.content.lower().strip() == "hey, please do not delete your messages.":
        # Private message the user who deleted the message
        user = message.author
        await user.send("You deleted the message: 'Hey, please do not delete your messages.'")

# Run the bot with the token
bot.run('YOUR_BOT_TOKEN')

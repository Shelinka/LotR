import discord

client = discord.Client()
token = 'MTA4OTI3Mzc3ODIyOTQ4OTc5NQ.Gcy_2X.hEUkzIdzBrZKJ4rK7LIDfawxKf9xKzqn7HrnGc'

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}!')

@client.event
async def on_message_delete(message):
    # Check if the message was in a channel with a mentionable role
    channel = message.channel
    guild = channel.guild
    mentionable_roles = [role for role in guild.roles if role.mentionable]
    if not mentionable_roles or not isinstance(channel, discord.TextChannel):
        return

    # Check if any mentionable role has permissions to mention everyone
    roles_with_mention_permission = [role for role in mentionable_roles if channel.permissions_for(role).mention_everyone]
    if not roles_with_mention_permission:
        return

    # Send a warning message to the user who deleted the message
    author = message.author
    warning_message = f'Hey {author.mention}, don\'t delete your pings!'
    try:
        await author.send(warning_message)
    except discord.errors.Forbidden as err:
        print(f'Failed to send warning message to {author.name}: {err}')

client.run(token)

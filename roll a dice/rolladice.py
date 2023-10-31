import discord
from discord.ext import commands
import random

@bot.event
async def on_ready():
    print(f"Bot is ready {bot.user.name}")
    # Initialize the last_bot_roll with a random value when the bot is ready
    # This is because if Channels are cleared or bot is used first time, it comes to Errors.
    bot.last_bot_roll = random.randint(1, 6)

@bot.command()
async def roll(ctx):
    # Check if the command is used in the 'roll-a-dice' channel  (CHANGE THIS TO YOUR CHANNELNAME)
    if ctx.channel.name is None or ctx.channel.name != 'roll-a-dice':
        await ctx.send("This command can only be used in the 'würfel' channel.")
        return

    # Generate a random roll for the user
    user_roll = random.randint(1, 6)

    # Compare the user's roll with the bot's last roll to determine the result
    result = "Tie!"
    if user_roll > bot.last_bot_roll:
        result = "Won!"
    elif user_roll < bot.last_bot_roll:
        result = "Lost!"

    # Send the result to the user
    await ctx.send(f'You rolled a {user_roll}, the bot rolled a {bot.last_bot_roll}. You {result}.')

    #OPTIONAL'
    #This is pretty optional in case you want to delete the Users msg with "!roll"
    # Delete the user's message to keep the channel clean
    #await ctx.message.delete()

    # Update the bot's last roll with the user's roll
    bot.last_bot_roll = user_roll

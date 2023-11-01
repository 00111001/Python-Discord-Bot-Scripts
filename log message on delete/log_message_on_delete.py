import discord
import time

intents = discord.Intents.default()
intents.message_content = True

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"User: {message.author.name} | Message: {message.content} | Time: {current_time}\n"

    with open("message_log.txt", "a+") as file:
        file.write(log_message)

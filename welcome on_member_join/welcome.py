# intents.members = True has to be activated

@bot.event
async def on_member_join(member):
    welcome_channel_id = "YOUR_CHANNEL_ID"
    if welcome_channel_id:
        welcome_channel = member.guild.get_channel(welcome_channel_id)

        if welcome_channel:
            welcome_message = (
                f"Welcome {member.mention} to our server! We're glad to have you here.\n\n"
                f"Please read our rules in <#YOUR_RULES_CHANNEL_ID> and introduce yourself in <#YOUR_INTRODUCTION_CHANNEL_ID>."
            )
            await welcome_channel.send(welcome_message)
        else:
            print("Welcome channel not found. Please check the channel ID.")
    else:
        print("Welcome channel ID is not defined. Please configure it.")

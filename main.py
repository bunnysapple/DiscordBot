import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("the bot is now ready for use")
    print(".\n..\n...\n....\n")

@client.event
async def on_member_join(member):
    channel = client.get_channel(int(CHANNEL_ID))
    await channel.send(f"Good to see you {member.mention}!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(int(CHANNEL_ID))
    await channel.send(f"Goodbye {member}")
    await channel.send("""Another one bites the dust\n
Another one bites the dust\n
And another one gone, and another one gone\n
Another one bites the dust (yeah)\n
Hey, I'm gonna get you too\n
Another one bites the dust\n""")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the Tutorial Bot")

@client.command()
async def bye(ctx):
    await ctx.send("Goodbye, have fun")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You must be in a voice channel to run this command... Join a voice channel.")

@client.command(pass_content = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice chat")
    else:
        await ctx.send("I am not in a voice chat")

client.run(TOKEN)
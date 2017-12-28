import discord
import asyncio

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
	print("ready")
	
@client.event
@asyncio.coroutine
def on_message(message):
	if message.content.startswith("!eve-item-lookup"):
		
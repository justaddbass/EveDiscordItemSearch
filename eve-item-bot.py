import discord
import asyncio
import item_lookup

tokenFile = open('token.txt', 'r')
token = tokenFile.read()
tokenFile.close()

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
	print('ready')
	
@client.event
@asyncio.coroutine
def on_message(message):
	if message.content.startswith('!eve-item-lookup search'):
		category = message.content.split('!eve-item-lookup search ')[1]
		pt = item_lookup.getItemsInCategory(category)
		yield from client.send_message(message.channel, pt)
	else:
		yield from client.send_message(message.channel, 'invalid command')
	if message.content.startswith('!quit'):
		client.logout()
		client.close()
		
client.run(token)
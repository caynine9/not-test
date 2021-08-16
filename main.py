#imports discord.py, allows access to discord's api
import discord

#import os module
import os

#imports random
import random

#import load_dotenv function from dotenv module.
from dotenv import load_dotenv

#loads the .env file that resides on the same level as the script.
load_dotenv()

#grab the api token from the .env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

#gets the client object from discord.py, client is synonymous with bot.
bot = discord.Client()

client = discord.Client()

#event listener for when the bot has switched from offline to online.
@bot.event
async def on_ready():
	#creates a counter to keep track of how many guilds/servers the bot is connected to.
	guild_count = 0

	#loops through all the guild/servers that the bot is associated with.
	for guild in bot.guilds:
		#print the server's id and name
		print(f" - {guild.id} (name: {guild.name})")

		#increments the guild counter.
		guild_count = guild_count + 1

		#prints how many guilds/servers the bot is in.
		print("Welcome Tantowi. Gucci Gang is in " + str(guild_count) + " guilds.")

	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Gucci Gang - Lil Pump"))


#event listener for when a new message is sent to a channel
@bot.event
async def on_message(message):

	if "hello" in message.content:
		if message.author.id == (175482613241348096):
			rudea = ('gausah sok akrab','bacot','ngok')
			await message.channel.send(random.choice(rudea))
		elif message.author.id == (696623194286587964):
			await message.channel.send("apa hendro sayang?:heart:")
		elif message.author.id == (323335776932724736):
			await message.channel.send("apa yoga sayang?:heart:")
		elif message.author.id == (607917820587671566):
			await message.channel.send("hello, my little pogchamp:heart:")

	elif message.content == "yoga":
		await message.channel.send("yoga sayang:heart:")
	
	elif "uwais" in message.content:
		await message.channel.send("***UWAIS***")

	elif "profil" in message.content:
		await message.channel.send("bacot kd usah dibahas")

	elif message.author.id == (696623194286587964):
		hendroa = ('<@696623194286587964> apa kabar nanda hen?','<@696623194286587964> apa kabar bita hen?','<@696623194286587964> jomblo mulu, kapan punya pacar?')
		await message.channel.send(random.choice(hendroa))

	elif message.author.id == (607917820587671566):
		haikala = ('<@607917820587671566> bacot wibu','<@607917820587671566> tahu kontol lah','<@607917820587671566> nyawa ni bisi ja kah pacar')
		await message.channel.send(random.choice(haikala))

	elif message.author.id == (323335776932724736):
		yogaa = ('<@323335776932724736> apa kabar nada? :laugh:','<@323335776932724736> jangan begadang sampe 3 hari','<@323335776932724736> hai sayangku :heart: -nada')
		await message.channel.send(random.choice(yogaa))
	
	elif "bungul" in message.content:
		if message.author.id == (175482613241348096):
			await message.channel.send("<@175482613241348096> kontol")

	elif message.author.id == (333885327242559488):
		aryaa = ('<@333885327242559488> hai arya sayang :heart:','oppa saranghae <@333885327242559488>','hai <@333885327242559488>')
		await message.channel.send(random.choice(aryaa))	

#executes the bot
bot.run("")

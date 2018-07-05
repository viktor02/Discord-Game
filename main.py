import discord
import asyncio

client = discord.Client()
login = input("Your discord email: ")
password = input("Your discord password: ")
selGame = input("Choose the game: ")
@client.event
async def on_ready():
    print('Logged in as')
    print('Your nickname: '+client.user.name)
    print('Your id: '+client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name=selGame))
    print('Game setted.')
try:
	client.run(login, password)
	print("Login succesful.")
except discord.errors.LoginFailure:
	print("login or password is incorrect.")

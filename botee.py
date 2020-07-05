import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
    print("Thank you for using Rex Buyer")
    await client.change_pressence(game=discord.Game(name="videos"))
    @client.event
    async def on_message(message):
        if message.content.startswith('!buy'):
            msg = 'Hello Please Message @Infinity For All Details Or Pay me at paypal Insanitogames@gmail.com  (0.author.mention) Enjoy Unknown Venom Admin If You Do Buy :)'.format(message)
            await client.send_message(message.channel, msg)

        if message.content.startswith('!steal everyones money'):
            msg = 'OOO give me some of that money youre so rich (0.author.mentaion)'.format(message)
            await client.send_message(message.channel, msg)

            if message.content.startswith('!snitch on the guy who stole money'):
            msg = 'OH DE POLICE LA DE DA OH THE POLICE ARRESTED MY CAR!!'.format(message)
            await client.send_message(message.channel, msg)

            if message.content.startswith('!commands','!cmds'):
            msg = 'Hello (0.author.mention) The Commands Are, !buy, !steal everyones money, and !snitch on the guy who stole money'.format(message)
            await client.send_message(message.channel, msg)

        client.run(os.getenv('NzI5MTcwMjgwOTc0NTE2MjM0.XwFf2Q.D-pJT2WK7GhGOSS9z_AncoYLLfY'))

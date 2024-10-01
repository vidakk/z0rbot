import os
import discord
import datetime

discordToken = os.environ.get('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user:
            return
        print(f'Message from {message.author}: {message.content}')
        c_channel = discord.utils.get(message.guild.text_channels, name='bot-testing')
        messages = [message async for message in c_channel.history(limit=2)]

        if messages[0].content == 'z':
            if messages[1].content == 'z':
                await c_channel.send(f'Hey, looks like {messages[0].author.display_name} fucked up the z0r chain! Everyone laugh at them! ')
                await message.author.timeout(datetime.timedelta(seconds=60))
        elif messages[0].content == '0':
            if messages[1].content == 'z':
                return
            else:
                await c_channel.send(f'Hey, looks like {messages[0].author.display_name} fucked up the z0r chain! Everyone laugh at them! ')
                await message.author.timeout(datetime.timedelta(seconds=60))
        elif messages[0].content == 'r':
            if messages[1].content == '0':
                return
            else:
                await c_channel.send(f'Hey, looks like {messages[0].author.display_name} fucked up the z0r chain! Everyone laugh at them! ')
                await message.author.timeout(datetime.timedelta(seconds=60))
        else:
            await c_channel.send(f'Hey, looks like {messages[0].author.display_name} fucked up the z0r chain! Everyone laugh at them! ')
            await message.author.timeout(datetime.timedelta(seconds=60))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discordToken)
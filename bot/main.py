import os
import discord
import datetime
from dotenv import load_dotenv
import random

load_dotenv()
discordToken = os.environ.get('DISCORD_TOKEN')
botChannel = os.environ.get('DISCORD_BOT_CHANNEL')
class MyClient(discord.Client):

    async def brokenChain(self,channel,message):

        messageList = [
            "Hey, looks like {name} fucked up the z0r chain! Everyone laugh at them!",
            "Some people can follow simple instructions. {name} apparently isn't one of them",
            'Navigating the current political landscape is hard, navigating the current z0r chain is not, {name}!',
            'Then God looked over all he had made, and he saw that {name} had fucked it up',
            'Once upon a time there was a z0r chain. "Was" because you fucked it up {name}',
            'And I looked, and behold a pale horse: and his name that sat on him was Death, and Failure followed with him. Your failure, {name}',
            "Enemies are red, allies are blue, {name} cant z0r, so it\'s a timeout for you",
            'Do you want a doomsday today, {name}?'
        ]

        selectedMessage = random.choice(messageList).format(name=message.author.display_name)

        try:
            await channel.send(selectedMessage)
            #await channel.send(f'Hey, looks like {message.author.display_name} fucked up the z0r chain! Everyone laugh at them! ')
            #await message.author.timeout(datetime.timedelta(seconds=60))
        except Exception as e:
            print(f'An error has occurred: {str(e)}')

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        c_channel = discord.utils.get(message.guild.text_channels, name=botChannel)

        if message.author == client.user:
            return

        if message.channel == c_channel:
            print(f'Message from {message.author}: {message.content} in {message.channel}')
            messages = [message async for message in c_channel.history(limit=2)]

            if len(messages) < 2:
                return  # Ensure there are at least two messages to compare

            async def default_action():
                await self.brokenChain(c_channel, message)
            async def doNothing():
                pass


            switch = {
                'z': lambda: self.brokenChain(c_channel, message) if messages[1].content == 'z' else doNothing(),
                '0': lambda: doNothing() if messages[1].content == 'z' else self.brokenChain(c_channel, message),
                'r': lambda: doNothing() if messages[1].content == '0' else self.brokenChain(c_channel, message)
            }

            action = switch.get(messages[0].content, default_action)
            await action()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discordToken)
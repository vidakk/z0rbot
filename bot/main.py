import os
import discord
import datetime
from dotenv import load_dotenv
import random

load_dotenv()
discordToken = os.environ.get('DISCORD_TOKEN')
class MyClient(discord.Client):

    async def brokenChain(self,channel,message):

        messageList = [
            'Hey, looks like {name} fucked up the z0r chain! Everyone laugh at them!',
            "Some people can follow simple instructions. {name} apparently isn't one of them",
            'Navigating the current political landscape is hard, navigating the current z0r chain is not, {name}!',
            'Then God looked over all he had made, and he saw that {name} had fucked it up'
        ]

        selectedMmessage = random.choice(messageList).format(name=message.author.display_name)

        #try:
        await channel.send(selectedMmessage)
            #await channel.send(f'Hey, looks like {message.author.display_name} fucked up the z0r chain! Everyone laugh at them! ')
        await message.author.timeout(datetime.timedelta(seconds=60))
        #except Exception as e:
            #print("an error occured")

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        c_channel = discord.utils.get(message.guild.text_channels, name='bot-testing')

        if message.author == client.user:
            return

        if message.channel == c_channel:
            print(f'Message from {message.author}: {message.content} in {message.channel}')
            messages = [message async for message in c_channel.history(limit=2)]

            if messages[0].content == 'z':
                if messages[1].content == 'z':
                    await self.brokenChain(c_channel,message)
            elif messages[0].content == '0':
                if messages[1].content == 'z':
                    return
                else:
                    await self.brokenChain(c_channel,message)

            elif messages[0].content == 'r':
                if messages[1].content == '0':
                    return
                else:
                    await self.brokenChain(c_channel,message)
            else:
                await self.brokenChain(c_channel,message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discordToken)
import discord
import os
from importlib import import_module as _import
import logging

logging.basicConfig(level=logging.INFO)

client = discord.Client()

CMDCHAR = '!'
COMMAND_PATH = os.path.join(os.path.dirname(__file__), 'Commands')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    text_channel_list = []
    for server in client.guilds:
        for channel in server.channels:
            if channel in server.text_channels:
                text_channel_list.append(channel)

    if message.content.startswith(CMDCHAR) and message.author != client.user:
        cmd, *args = message.content[1:].split(' ')
        print('Command Received: ' + cmd)
        for root, dirs, files in os.walk(COMMAND_PATH):
            cmd_file = cmd + '.py'
            print(files, cmd_file)
            if cmd_file in files:
                module = _import('Commands.' + cmd)
                for c in text_channel_list:
                    await getattr(module, cmd)(client, c, *args)
                print("Done")
                break


client.run('NzkzMzkxODE5MTA2NTQ5Nzcx.X-rltg.-nrGD9-zHzOKgU0kVsR4Z9xESz8')

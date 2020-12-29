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
    for server in Client.servers:
        for channel in server.channels:
            if channel.type == 'Text':
                text_channel_list.append(channel)

    if message.content.startswith(CMDCHAR) and message.author != client.user:
        cmd, *args = message.content[1:].split(' ')
        print('Command Received: ' + cmd)
        for root, dirs, files in os.walk(COMMAND_PATH):
            cmd_file = cmd + '.py'
            print(files, cmd_file)
            if cmd_file in files:
                module = _import('Commands.' + cmd)
                for channel in text_channel_list:
                    await getattr(module, cmd)(client, channel, *args)
                break


client.run('NzkzMzkxODE5MTA2NTQ5Nzcx.X-rltg.3y5s9x5Ey60x2aO6ocdbDwVFIMI')

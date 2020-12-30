import os

async def parse(client, channel, *args):
    try:
        path = './Parsed/%s' % channel.id
        os.makedirs(path)
        # await channel.send('Beginning parsing of channel logs.')

        user_path = path + '/{}.txt'.format(channel.id)
        with open(user_path, 'a+') as f:
            async for message in channel.history(limit=None):
                if 'EPIC GUARD' in message.content and message.attachments:
                    author = message.author.id
                    print(author)
                    print(message.content)
                    if author == 555955826880413696:
                        if channel.id not in opened_files:
                            f.write('{}\n'.format(message.attachments[0].url))
                            print(message.attachments)
                        else:
                            for channel.id, file in opened_files.items():
                                print("closing file {}".format(str(file)))
                                file.close()
                            return 0
    
    except Exception as e:
        print(e)
        return 0


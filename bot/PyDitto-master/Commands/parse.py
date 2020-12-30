import os

async def parse(client, channel, *args):
    try:
        path = './Parsed/%s' % channel.id
        os.makedirs(path)
        # await channel.send('Beginning parsing of channel logs.')

        opened_files = dict()
        async for message in channel.history(limit=None):
            if 'EPIC GUARD' in message.content and message.attachments:
                author = message.author.id
                print(author)
                print(message.content)
                if author == 555955826880413696:
                    user_path = path + '/{}.txt'.format(author)
                    if author not in opened_files:
                        with open(user_path, 'a+') as f:
                            f.write('{}\n'.format(message.attachments[0].url))
                            print(message.attachments)
                    else:
                        for author, file in opened_files.items():
                            file.close()
                        return 0
                        # return await channel.send('Finished parsing.')

    except Exception as e:
        print(e)
        return 0

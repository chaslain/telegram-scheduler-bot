from telegram import Bot
from os import getenv

token = getenv("BOT_TOKEN")

bot = Bot(token)

updates = bot.get_updates()

print("have updates", len(updates))

for update in updates:
    message = update['message']

    if message == None:
        print("no message in update")
        continue

    if message['video'] != None:
        print(message['video']['file_id'])
    
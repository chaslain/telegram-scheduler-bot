from telegram import Bot
from os import getenv

token = getenv("BOT_TOKEN")

bot = Bot(token=token)

id = None

updates = bot.get_updates(id)

while len(updates) > 0:
    print("Clearing " + str(len(updates)) + " updates")
    updates = bot.get_updates(updates[-1]['update_id']+1)



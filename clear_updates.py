import os
import telegram

token = os.getenv("BOT_TOKEN")

if token == None:
    print("Provide token")
    token = input()

bot = telegram.Bot(token)

current_id = None
while True:
    updates = bot.getUpdates(current_id)
    current_id = updates[49].update_id
    if len(updates) != 100:
        break
    

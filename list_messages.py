import os
import telegram

token = os.getenv("BOT_TOKEN")

if token == None:
    print("Provide token")
    token = input()

target_from_user = os.getenv("TARGET_FROM_USER")

if target_from_user == None:
    print("No target user specified")
    exit()
else:
    target_from_user = int(target_from_user)

bot = telegram.Bot(token)

updates = bot.getUpdates()
length = len(updates)

print("processing " + str(length) + " updates") 

for i, update in enumerate(updates):
    if update.message != None:
        message = update.message
        if message.video != None:
            if message.from_user.id == target_from_user:
                video = message.video
                print(video.file_id)
    
    if i == length - 1:
        print("most recent update id: " + str(update.update_id))
        bot.getUpdates(update.update_id)
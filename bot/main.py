from logging import exception
import telegram
import bot.FileCandidateManager
import bot.CredentialManager
import os

class Main:
    def __init__(self, bot, weekday):
        self.bot = bot
        self.weekday = weekday


    def getBot(self) -> telegram.bot.Bot:
        return self.bot
    
    def main(self):
        fcm = bot.FileCandidateManager.FileCandidateManager("data")
        filePath = fcm.getCandidateFileName(self.weekday)

        if filePath == None:
            return
        file = open(filePath, "rb")

        if not os.path.exists("data"):
            exception("No data provided.")
        
        try:
            self.getBot().send_document(chat_id=bot.CredentialManager.CredentialManager.getChatId(), document=file)
        except BaseException as e:
            print(e)
            pass;
        
        file.close()
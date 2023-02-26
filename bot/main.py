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
        fcm = bot.FileCandidateManager.FileCandidateManager("data2")
        filePath = fcm.getCandidateFileName(self.weekday)

        if filePath == None:
            return
        
        data = None
        with open(filePath, "r") as file:
            data = file.read()
        
        try:
            self.getBot().send_video(chat_id=bot.CredentialManager.CredentialManager.getChatId(), video=data)
        except BaseException as e:
            print(e)
            pass;
        
        file.close()
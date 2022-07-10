from logging import exception
import telegram
import bot.FileCandidateManager
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

        fileContent = None
        with open("data/" + filePath, "rb") as file:
            fileContent = file.readlines()

        if not os.path.exists("data"):
            exception("No data provided.")
        
        self.getBot().send_document(fileContent)
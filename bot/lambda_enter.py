import bot.main
import telegram
import bot.CredentialManager
import datetime

def handler(Event, Context):
    bot = telegram.Bot(bot.CredentialManager.CredentialManager.getCredential())
    bot.main.Main(bot, datetime.datetime().weekday) \
    .main()



import bot.main
import telegram
import bot.CredentialManager
import datetime

def handler(Event, Context):
    tbot = telegram.Bot(bot.CredentialManager.CredentialManager.getCredential())
    bot.main.Main(tbot, datetime.datetime.today().weekday()) \
    .main()



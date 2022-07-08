import main
import telegram
import CredentialManager
import datetime

def handler(Event, Context):
    bot = telegram.Bot(CredentialManager.CredentialManager.getCredential())
    main.Main(bot, datetime.datetime().weekday) \
    .main()



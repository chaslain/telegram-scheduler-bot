import bot.main
import telegram


day = input("Please put weekday - 0 is Monday, 6 is Sunday\n");
tbot = telegram.Bot(bot.CredentialManager.CredentialManager.getCredential())
bot.main.Main(tbot, int(day)) \
.main()
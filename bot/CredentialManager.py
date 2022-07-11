
from logging import exception
from tokenize import String
import sys
import os


class CredentialManager:

    token = None
    chat_id = None

    def getChatId() -> str:
        if CredentialManager.chat_id == None:
            CredentialManager.chat_id = os.getenv("CHAT_ID")
            if (CredentialManager.chat_id == None):
                exception("NO CHAT ID PROVIDED")
        return CredentialManager.chat_id

    def getCredential() -> str:
        if CredentialManager.token == None:
            CredentialManager.token = os.getenv("BOT_TOKEN")
            if CredentialManager.token == None:
                exception("NO BOT TOKEN PROVIDED")
        return CredentialManager.token
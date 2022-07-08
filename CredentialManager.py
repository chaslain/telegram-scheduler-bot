
from logging import exception
from tokenize import String
import sys
import os


class CredentialManager:

    token = None

    def getCredential() -> str:
        if CredentialManager.token == None:
            token = os.getenv("BOT_TOKEN")
            if token == None:
                exception("NO BOT TOKEN PROVIDED")
        return token
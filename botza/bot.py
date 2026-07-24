from .client import TelegramClient


class Bot:
    def __init__(self, token: str):
        self.client = TelegramClient(token)

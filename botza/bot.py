from .api.methods import APIMethods
from .client import TelegramClient


class Bot(APIMethods):
    def __init__(self, token: str):
        self.client = TelegramClient(token)

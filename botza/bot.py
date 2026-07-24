from .client import TelegramClient
from .api.methods import APIMethods


class Bot(APIMethods):
    def __init__(self, token: str):
        self.client = TelegramClient(token)
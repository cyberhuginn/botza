from .api.messages import MessageMethods
from .api.users import UserMethods
from .client import TelegramClient


class Bot(
    UserMethods,
    MessageMethods,
):
    def __init__(self, token: str):
        self.client = TelegramClient(token)

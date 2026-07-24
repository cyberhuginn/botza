from .api.media import MediaMethods
from .api.messages import MessageMethods
from .api.updates import UpdateMethods
from .api.users import UserMethods
from .client import TelegramClient


class Bot(
    UserMethods,
    MessageMethods,
    MediaMethods,
    UpdateMethods,
):
    def __init__(self, token: str):
        self.client = TelegramClient(token)

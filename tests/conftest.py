from unittest.mock import AsyncMock

import pytest

from botza.api.messages import MessageMethods
from botza.api.updates import UpdateMethods
from botza.api.users import UserMethods


class DummyBot(
    UserMethods,
    MessageMethods,
    UpdateMethods,
):
    def __init__(self):
        self.client = AsyncMock()


@pytest.fixture
def bot():
    return DummyBot()

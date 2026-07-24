from unittest.mock import AsyncMock

import pytest

from botza.api.methods import APIMethods


@pytest.mark.asyncio
async def test_send_message():
    client = AsyncMock()

    client.request.return_value = {
        "message_id": 1,
        "chat": {
            "id": 123,
        },
        "text": "Hello",
    }

    api = APIMethods(client)

    result = await api.send_message(
        chat_id=123,
        text="Hello",
    )

    client.request.assert_called_once_with(
        "sendMessage",
        chat_id=123,
        text="Hello",
    )

    assert result["message_id"] == 1

from unittest.mock import AsyncMock
import pytest

from botza.api.methods import APIMethods


@pytest.mark.asyncio
async def test_send_message_with_parse_mode():
    client = AsyncMock()
    client.request.return_value = {"message_id": 1}

    api = APIMethods(client)

    await api.send_message(
        chat_id=123,
        text="<b>Hello</b>",
        parse_mode="HTML",
    )

    client.request.assert_called_once_with(
        "sendMessage",
        chat_id=123,
        text="<b>Hello</b>",
        parse_mode="HTML",
    )

import pytest


@pytest.mark.asyncio
async def test_send_message(bot):
    bot.client.request.return_value = {
        "message_id": 1,
    }

    result = await bot.send_message(
        chat_id=123,
        text="Hello",
    )

    bot.client.request.assert_called_once_with(
        "sendMessage",
        chat_id=123,
        text="Hello",
    )

    assert result["message_id"] == 1


@pytest.mark.asyncio
async def test_send_message_with_parse_mode(bot):
    bot.client.request.return_value = {
        "message_id": 1,
    }

    await bot.send_message(
        chat_id=123,
        text="<b>Hello</b>",
        parse_mode="HTML",
    )

    bot.client.request.assert_called_once_with(
        "sendMessage",
        chat_id=123,
        text="<b>Hello</b>",
        parse_mode="HTML",
    )

import pytest


@pytest.mark.asyncio
async def test_get_updates(bot):
    bot.client.request.return_value = {
        "ok": True,
        "result": [
            {
                "update_id": 123,
                "message": {
                    "text": "Hello",
                },
            }
        ],
    }

    result = await bot.get_updates()

    bot.client.request.assert_called_once_with(
        "getUpdates",
    )

    assert result == {
        "ok": True,
        "result": [
            {
                "update_id": 123,
                "message": {
                    "text": "Hello",
                },
            }
        ],
    }


@pytest.mark.asyncio
async def test_get_updates_with_params(bot):
    await bot.get_updates(
        offset=100,
        limit=50,
        timeout=30,
    )

    bot.client.request.assert_called_once_with(
        "getUpdates",
        offset=100,
        limit=50,
        timeout=30,
    )
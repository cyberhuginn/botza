import httpx

from botza.exceptions import TelegramError


class TelegramClient:
    BASE_URL = "https://api.telegram.org"

    def __init__(self, token: str):
        self.token = token

        self.client = httpx.AsyncClient(
            base_url=f"{self.BASE_URL}/bot{token}/",
            timeout=30,
        )

    async def request(self, method: str, **params):
        response = await self.client.post(
            method,
            json=params,
        )
        response.raise_for_status()
        data = response.json()
        if not data["ok"]:
            raise TelegramError(data)
        return data["result"]

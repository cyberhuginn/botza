class APIMethods:
    def __init__(self, client):
        self.client = client

    async def get_me(self):
        return await self.client.request("getMe")

    async def send_message(self, chat_id: int | str, text: str, **kwargs):
        return await self.client.request(
            "sendMessage",
            chat_id=chat_id,
            text=text,
            **kwargs,
        )

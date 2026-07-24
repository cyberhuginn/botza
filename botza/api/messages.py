class MessageMethods:
    async def send_message(
        self,
        chat_id: int | str,
        text: str,
        **kwargs,
    ):
        payload = {
            "chat_id": chat_id,
            "text": text,
            **kwargs,
        }

        return await self.client.request(
            "sendMessage",
            **payload,
        )

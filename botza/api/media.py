class MediaMethods:
    async def send_photo(
        self,
        chat_id: int | str,
        photo: str,
        **kwargs,
    ):
        payload = {
            "chat_id": chat_id,
            "photo": photo,
            **kwargs,
        }

        return await self.client.request(
            "sendPhoto",
            **payload,
        )

    async def send_document(
        self,
        chat_id: int | str,
        document: str,
        **kwargs,
    ):
        payload = {
            "chat_id": chat_id,
            "document": document,
            **kwargs,
        }

        return await self.client.request(
            "sendDocument",
            **payload,
        )

    async def send_video(
        self,
        chat_id: int | str,
        video: str,
        **kwargs,
    ):
        payload = {
            "chat_id": chat_id,
            "video": video,
            **kwargs,
        }

        return await self.client.request(
            "sendVideo",
            **payload,
        )

    async def send_audio(
        self,
        chat_id: int | str,
        audio: str,
        **kwargs,
    ):
        payload = {
            "chat_id": chat_id,
            "audio": audio,
            **kwargs,
        }

        return await self.client.request(
            "sendAudio",
            **payload,
        )

    async def send_voice(
        self,
        chat_id: int | str,
        voice: str,
        **kwargs,
    ):
        payload = {
            "chat_id": chat_id,
            "voice": voice,
            **kwargs,
        }

        return await self.client.request(
            "sendVoice",
            **payload,
        )

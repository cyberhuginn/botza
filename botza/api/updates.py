class UpdateMethods:
    async def get_updates(
        self,
        offset: int | None = None,
        limit: int | None = None,
        timeout: int | None = None,
        **kwargs,
    ):
        payload = {
            **kwargs,
        }

        if offset is not None:
            payload["offset"] = offset

        if limit is not None:
            payload["limit"] = limit

        if timeout is not None:
            payload["timeout"] = timeout

        return await self.client.request(
            "getUpdates",
            **payload,
        )

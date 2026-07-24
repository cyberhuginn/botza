class APIMethods:
    async def get_me(self):
        return await self.client.request("getMe")

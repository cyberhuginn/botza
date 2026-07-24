import asyncio
from decouple import config

from botza import Bot

TOKEN = config('TOKEN')


async def main():
    bot = Bot(TOKEN)
    me = await bot.get_me()
    print(me)


if __name__ == "__main__":
    asyncio.run(main())

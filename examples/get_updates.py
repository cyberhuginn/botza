import asyncio
from decouple import config

from botza import Bot


async def main():
    bot = Bot(config('TOKEN'))

    updates = await bot.get_updates(
        timeout=30,
        limit=10,
    )

    for update in updates:
        print(update)


if __name__ == "__main__":
    asyncio.run(main())

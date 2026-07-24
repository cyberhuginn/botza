import asyncio

from decouple import config

from botza import Bot


async def main():
    bot = Bot(config("TOKEN"))

    response = await bot.send_message(
        chat_id=config("CHAT_ID"),
        text="Hello from botza",
    )
    print(response)


asyncio.run(main())

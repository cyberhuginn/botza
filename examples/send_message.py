import asyncio

from decouple import config

from botza import Bot


async def main():
    bot = Bot(token=config("TOKEN"))

    message = await bot.send_message(
        chat_id=int(config("CHAT_ID")),
        text="Hello from Botza 🚀",
    )

    print(message)


if __name__ == "__main__":
    asyncio.run(main())

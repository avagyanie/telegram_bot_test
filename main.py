import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router


bot = Bot(token='8199257283:AAGkX7KNw9YNrx8YyrUl6TEsHfDdxfkslLE')
dp = Dispatcher()



async def main():
    dp.iclude_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")
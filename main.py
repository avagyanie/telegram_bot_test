import os
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router


bot = Bot(token=os.environ.get("TOKEN"))
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is off")

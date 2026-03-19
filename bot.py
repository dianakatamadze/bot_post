import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router

async def main():
    bot = Bot(token="8409980181:AAFSrGoyiT9WlUwDHJTzrxT8mxwlgDLS3Ls")
    dp = Dispatcher()

    dp.include_router(router)

    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
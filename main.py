import asyncio
from aiogram import Dispatcher
from bot import bot
from handlers.catalog.handler import router
from database.models import init_db

dp = Dispatcher()

dp.include_router(router)

async def main():
    await init_db()   
    await bot.delete_webhook(True)  
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

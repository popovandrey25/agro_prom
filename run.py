import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers.base_handler import router as base_router


async def main():
    load_dotenv()

    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_routers(base_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')

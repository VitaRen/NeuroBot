import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
import logging
from handlers import common, choice_profession


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.token)
    dp = Dispatcher()
    dp.include_router(common.router)
    dp.include_router(choice_profession.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
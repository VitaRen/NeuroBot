import asyncio
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import logging
import random

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.token)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет {name}')


@dp.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока {name}')


@dp.message(Command('info'))
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Этот бот создан для тренировки навыков и не несет существенной информации')


@dp.message(Command('user'))
async def cmd_user(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пользователь - {name}')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
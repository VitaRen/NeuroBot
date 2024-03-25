import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
from Keyboards import kb2
from RandomFox import fox

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



@dp.message(Command('fox'))
@dp.message(Command('лиса'))
@dp.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'{name} держи лису')
    await message.answer_photo(photo=img_fox)


@dp.message(F.text)
async def cmd_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if "привет" in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif "что ты умеешь делать" in msg_user:
        await message.answer("я ничего не умею, я еще не умный")
    elif "лиса" in msg_user:
        await message.answer(f'смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Ты написал - {msg_user}')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
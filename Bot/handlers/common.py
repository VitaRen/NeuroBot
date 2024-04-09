from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
from Bot.keyboards.keyboards import kb2
from Bot.utils.RandomFox import fox

router = Router()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет {name}')


@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока {name}')


@router.message(Command('info'))
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Этот бот создан для тренировки навыков и не несет существенной информации')


@router.message(Command('user'))
async def cmd_user(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пользователь - {name}')



@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'{name} держи лису')
    await message.answer_photo(photo=img_fox)


@router.message(F.text)
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
from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Bot.keyboards.prof_keyboards import make_row_keyboard


router = Router()

prof_name = ['Разработчик', 'Аналитик', 'Тестировщик']
prof_grades = ['Junior', 'Middle', 'Senior']

@router.message(Command('/prof'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет {name}, выбери профессию', reply_markup=make_row_keyboard(prof_name))
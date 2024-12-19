from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards as kb
from app.states import Start

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Start.menu)
    await message.answer('ПРИВЕТ ВЫБЕРИ', reply_markup=kb.reply_menu)


@router.message(Start.menu, F.text == 'Задать вопрос')
async def ask_question(message: Message, state: FSMContext):
    await state.set_state(Start.chat)
    await message.answer(
        'Задайте вопрос',
        reply_markup=kb.reply_back
    )


@router.message(Start.chat, F.text == 'Назад')
async def stop_chat(message: Message, state: FSMContext):
    await state.set_state(Start.menu)
    await message.answer(
        'ВЫБЕРИ',
        reply_markup=kb.reply_menu
    )


@router.message(Start.chat)
async def ask_question(message: Message, state: FSMContext):
    await message.answer(
        'ответ модели'
    )


@router.message(Start.menu, F.text == 'Получить чек-лист')
async def check_list(message: Message, state: FSMContext):
    await state.set_state(Start.checklist)
    await message.answer(
        'держи чек лист друг тракторист',
        reply_markup=kb.reply_menu
    )
    await state.set_state(Start.menu)

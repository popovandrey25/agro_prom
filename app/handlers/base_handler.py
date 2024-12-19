from aiogram import Router
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

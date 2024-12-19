from aiogram.fsm.state import State, StatesGroup


class Start(StatesGroup):
    menu = State()
    chat = State()
    checklist = State()

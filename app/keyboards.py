from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reply_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Задать вопрос')],
        [KeyboardButton(text='Получить чек-лист')]
    ],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню.',
    one_time_keyboard=True
)
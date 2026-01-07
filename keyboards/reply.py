# главная и основня клавиатура
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text='Каталог🥦') 
        ],
        [
           
            KeyboardButton(text='Помощь💪')
        ]
    ],    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Нажмите интересующую кнопку...' 
)


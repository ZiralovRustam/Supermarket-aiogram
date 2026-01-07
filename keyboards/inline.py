from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# тоже важная клавиатура. список возможностей.
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Овощи. Фрукты🥬', callback_data='fruits'),
            InlineKeyboardButton(text='Мясо🥩', callback_data='meat')
        ],
        [
            InlineKeyboardButton(text='Десерты🥐', callback_data='deserts')
        ]
    ]
)

# клавиатура для десертов
deserts_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Торт', callback_data='cake'),
            InlineKeyboardButton(text='Круассaн', callback_data='croissant')
        ],
        [
            InlineKeyboardButton(text='Кекс', callback_data='cupcake')
        ],
        [
            InlineKeyboardButton(text='Назад⬅️', callback_data='back_catalog')
        ]
    ]
)

# отдельная клавиатура для торта
cake_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Наполеон', callback_data='napoleon'),
            InlineKeyboardButton(text='Блинный', callback_data='blin')
        ],
        [
            InlineKeyboardButton(text='Назад⬅️', callback_data='back_catalog')
        ]
    ]
)

# отдельная клавиатура для кекса
cupcake_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Шоколадный', callback_data='chokolate'),
            InlineKeyboardButton(text='Кремовый', callback_data='cream')
        ],
        [
            InlineKeyboardButton(text='Назад⬅️', callback_data='back_catalog')
        ]
    ]
)

# основная клавиатура для овощей
vegetables_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Помидор', callback_data='tomat'),
            InlineKeyboardButton(text='Огурец', callback_data='cucumber')
        ],
        [
            InlineKeyboardButton(text='Яблоки', callback_data='apple'),
            InlineKeyboardButton(text='Вишня', callback_data='cherry')
        ],
        [
            InlineKeyboardButton(text='Назад⬅️', callback_data='back_catalog')
        ]
    ]
)

# клавиатура для мяса
meat_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Говядина', callback_data='beaf'),
            InlineKeyboardButton(text='Курица', callback_data='chicken')
        ],
        [
            InlineKeyboardButton(text='Назад⬅️', callback_data='back_catalog')
        ]
    ]
)

# килограммы
meat_kg_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1 Килограмм', callback_data='kg1'),
            InlineKeyboardButton(text='2 Килограмма', callback_data='kg2')
        ],
        [
            InlineKeyboardButton(text='3 Килограмма', callback_data='kg3')
        ],
        [
            InlineKeyboardButton(text='Назад⬅️', callback_data='back_catalog')
        ]
    ]
)

# способы оплаты
pay_type_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оплатить звездами⭐', callback_data='star')
        ],
        [
            InlineKeyboardButton(text='Назад⬅️', callback_data='back_catalog')
        ]
    ]
)

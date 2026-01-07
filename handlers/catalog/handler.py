from aiogram.filters import Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, CallbackQuery
from aiogram import F, Router
import keyboards.reply as reply_kb
import keyboards.inline as inline_kb
from aiogram.types import FSInputFile
from bot import bot
from database.models import async_session, Payment
router = Router()

# стартовый хэндлер
@router.message(Command('start'))
async def start(message: Message):
    photo = FSInputFile('png-klev-club-hz3x-p-supermarket-png-1.png') 
    await message.answer_photo(
        photo=photo,
        caption=(
            f'Добро пожаловать, {message.from_user.first_name}! 🍕\n'
            'Это супер-маркет.\n'
            '👇 Нажми нужную кнопку.'
        ),
        reply_markup=reply_kb.reply_kb
    )

# ловим каталог
@router.message(F.text == 'Каталог🥦')
async def catalog(message: Message):
    await message.answer('Вот наш выбор👇', reply_markup=inline_kb.inline_kb)

@router.callback_query(F.data == 'back_catalog')
async def back_to_catalog(callback: CallbackQuery):
    await callback.message.edit_text(
        'Вот наш выбор👇',
        reply_markup=inline_kb.inline_kb
    )
    
# вывод текста и клавиатур для фруктов
@router.callback_query(F.data == 'fruits')
async def fruits(callback: CallbackQuery):
    await callback.message.edit_text(
        'Решили купить что-то полезноe🥦.Отлично! Вот наш выбор👇',
        reply_markup=inline_kb.vegetables_kb
    )

@router.callback_query(F.data.in_({'tomat','cherry','cucumber','apple'}))
async def good_food(callback: CallbackQuery):
    text = {
        'tomat': 'Отлично!Теперь можно оплатить покупку',
        'cherry': 'Отлично!Теперь можно оплатить покупку',
        'apple': 'Отлично!Теперь можно оплатить покупку',
        'cucumber': 'Отлично!Теперь можно оплатить покупку',
    }
    await callback.message.answer(text[callback.data],reply_markup=inline_kb.pay_type_kb)

# вывод текста и клавиатур для десертов
@router.callback_query(F.data == 'deserts')
async def deserts(callback: CallbackQuery):
    await callback.message.edit_text(
        'Десерты🎂. Отличный выбор!\n Вот что у нас в наличии.',
        reply_markup=inline_kb.deserts_kb
    )

@router.callback_query(F.data.in_({'cake','cupcake','croissant'}))
async def sweets_choice(callback: CallbackQuery):
    texts = {
        'cake': 'Мммм. Торт🎂',
        'cupcake': 'Кексы🤩. Объеденье',
        'croissant': 'Круассаны. Вкуснятина😛',
    }
    sweets_kb = {
        'cake': inline_kb.cake_kb,
        'cupcake': inline_kb.cupcake_kb,
    }
    kb = sweets_kb.get(callback.data)
    await callback.message.answer(texts[callback.data], reply_markup=kb)
    await callback.message.answer(
        "Теперь выберите способ оплаты:",
        reply_markup=inline_kb.pay_type_kb

    )

@router.callback_query(F.data.in_({'napoleon', 'blin', 'chokolate', 'cream'}))
async def dessert_type(callback: CallbackQuery):
    await callback.message.answer(
        f"Вы выбрали: {callback.data} 🍰"
    )

# вывод текста и клавиатур для мяса
@router.callback_query(F.data == 'meat')
async def meat(callback: CallbackQuery):
    await callback.message.edit_text(
        'Мясо🥩.То что нужно!\n Вот что у нас в наличии.',
        reply_markup=inline_kb.meat_kb
    )

@router.callback_query(F.data.in_({'beaf','chicken'}))
async def meat_choice(callback: CallbackQuery):
    texts = {
        'beaf': 'Хорошо. Выбери сколько килограмм тебе нужно',
        'chicken': 'Хорошо. Выбери сколько килограмм тебе нужно'
    }
    myaso_kb = {
        'chicken': inline_kb.meat_kg_kb,
        'beaf': inline_kb.meat_kg_kb,
    }
    kb = myaso_kb.get(callback.data)
    await callback.message.answer(texts[callback.data], reply_markup=kb)
    await callback.message.answer(
        "Теперь выберите способ оплаты:",
        reply_markup=inline_kb.pay_type_kb
    )

@router.callback_query(F.data.in_({'kg1', 'kg2', 'kg3'}))
async def choose_weight(callback: CallbackQuery):
    await callback.message.answer(
        f"Вы выбрали {callback.data.replace('kg', '')} кг 👍"
    )

# оплата в звездах
@router.callback_query(F.data == 'star')
async def pay_star(callback: CallbackQuery):
    await callback.message.answer_invoice(
        title='Покупка продукта💰',
        description='Оплата вашего товара',
        payload=f'star_{callback.from_user.id}',
        currency='XTR',
        prices=[LabeledPrice(label='XTR', amount=1)] # цена
    )

@router.pre_checkout_query()
async def pre_check(event: PreCheckoutQuery) -> None:
    await event.answer(True)

@router.message(F.successful_payment)
async def successful_payment(message: Message) -> None: 
    payment = message.successful_payment
    async with async_session() as session:
        new_payment = Payment(
            telegram_id = message.from_user.id,
            username = message.from_user.username,
            amount = payment.total_amount,
            payload = payment.invoice_payload
            
        )
        # возрат звезды
        session.add(new_payment)
        await bot.refund_star_payment(
            message.from_user.id,
            payment.telegram_payment_charge_id
        )
        await message.answer(
            'Оплата прошла успешно! #звезды были возвращены, так как это тестовый бот.'
        )
        


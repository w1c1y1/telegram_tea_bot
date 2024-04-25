from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from random import randint
import kb
import text
import db

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    username = msg.from_user.username
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Помощь", callback_data="help"))
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=builder.as_markup())


@router.message(Command("catalog"))
async def start_handler(msg: Message):
    pay_button = types.InlineKeyboardButton(text="Оплата", pay=True)
    tea1 = types.InlineKeyboardButton(text="Шу Пуэр 'Пять Деревень' 357гр/2600р", callback_data="tea_id_1")
    tea2 = types.InlineKeyboardButton(text="Шу Пуэр, 'Лао Шу Цзинь Я' 357гр/2600р", callback_data="tea_id_2")
    order = types.InlineKeyboardButton(text="Заказ", callback_data="order")
    next_page = types.InlineKeyboardButton(text="Следующая страница", callback_data="next_catalog_page")
    data = [[pay_button], [tea1], [tea2], [order], [next_page]]
    builder = InlineKeyboardMarkup(inline_keyboard=data)
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=builder)


@router.callback_query(F.data == "help")
async def help_user(callback: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Назад", callback_data="help_return"))
    await callback.message.answer(text.help, reply_markup=builder.as_markup())


@router.callback_query(F.data == "help_return")
async def back_to_main(callback: types.Message):
    username = callback.message.from_user.username

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Помощь", callback_data="help"))
    await callback.message.answer(text.greet.format(name=callback.message.from_user.full_name),
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data == "tea_id_1")
async def tea_list(callback: types.CallbackQuery):
    data = F.data
    user_id = callback.from_user.id
    tea_name = db.get_tea_name(data)
    request = list(db.get_tea_from_db(tea_name))
    db.add_orders_to_db(user_id, request)


@router.callback_query(F.data == "tea_id_2")
async def tea_list(callback: types.CallbackQuery):
    data = F.data
    user_id = callback.from_user.id
    tea_name = db.get_tea_name(data)
    request = list(db.get_tea_from_db(tea_name))
    db.add_orders_to_db(user_id, request)





from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.menu import menu
from loader import dp, db, bot
import re
import sqlite3

@dp.message_handler(CommandStart(deep_link='kunuz'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Assalomu alaykum,{message.from_user.full_name}!\n"
    text += f"Sizni {args} tavsiya qildi"
    await message.answer(text)

@dp.message_handler(CommandStart(deep_link='foydaliLink'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom,{message.from_user.full_name}!\n"
    text += f"Sizni {args} tavsiya qildi"
    await message.answer(text)

@dp.message_handler(CommandStart(deep_link=re.compile("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"Salom,{message.from_user.full_name}!\n"
    text += f"Siz {args} saytidan keldingiz"
    await message.answer(text)


@dp.message_handler(commands='start')
@dp.message_handler(text="/start")
@dp.message_handler(CommandStart())
@dp.edited_message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    if db.check_user(id=message.from_user.id):
        await message.answer(
            f"Assalomu alaykum,\nBotdan foydalanish uchun tugmalardan birini bosing",
            reply_markup=menu)
    else:
        try:
            db.add_user(id=message.from_user.id,
                        name=name)
            await bot.send_message(chat_id=ADMINS[0], text=f"Yangi foydalanuvchi: {message.from_user.full_name}\nFoydalanuvchilar soni: {db.count_users()[0]}")
        except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
        await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nBotdan foydalanish uchun tugmalardan birini bosing", reply_markup=menu)



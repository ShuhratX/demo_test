from aiogram import types
from keyboards.inline.katalog import KATALOG_1, KATALOG_2, CANCEL
from loader import dp, bot


@dp.message_handler(text_contains='Katalog')
async def katalog_1(message: types.Message):
    await message.answer(text="Maxsulot tanlang", reply_markup=KATALOG_1)


@dp.callback_query_handler(text_contains='next')
async def katalog_2(call: types.CallbackQuery):
    await call.message.edit_reply_markup(KATALOG_2)


@dp.callback_query_handler(text_contains='prev')
async def katalog_prev(call: types.CallbackQuery):
    await call.message.edit_reply_markup(KATALOG_1)


@dp.callback_query_handler(text_startswith='mega_')
async def item(call: types.CallbackQuery):
    number = call.data.split('_')[1]
    txt = call.data.split('_')[2]
    photo = open(f'img/{number}.jpg', 'rb')
    await call.message.edit_reply_markup()
    await call.message.answer_photo(photo, caption=txt, reply_markup=CANCEL)


@dp.callback_query_handler(text_contains='cancel')
async def cancelcheck(call: types.CallbackQuery):
    cap = call.message.caption
    cat = ''
    if 'Mega ' in cap:
        cat = KATALOG_1
    else:
        cat = KATALOG_2
    await call.message.delete()
    await call.message.answer(text="Maxsulot tanlang", reply_markup=cat)

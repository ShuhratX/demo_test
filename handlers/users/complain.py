from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from keyboards.default.menu import menu

from loader import dp, bot, db
from states.market_data import MarketData
from states.offer import Offer
from keyboards.inline.regions import REGIONS

# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text_contains="Shikoyat", state=None)
async def enter_test(message: types.Message):
    await message.answer("Tumaningizni tanlang", reply_markup=REGIONS)

    await MarketData.region.set()


@dp.message_handler(text_contains="Supervisor")
async def super(message: types.Message):
    await message.answer(text="Supervisor raqami: +998900944994")


# @dp.message_handler(Command(commands="Muslima", prefixes="!"))
# async def super(message: types.Message):
#     await message.answer(text="Muslima tentak-ku. Bechora Shuhratni sho'ri🤣")
#
#
@dp.message_handler(Command(commands="tuzuvchi", prefixes="!"))
async def super(message: types.Message):
    await message.answer(text="Bot tuzuvchi: Shuhrat Isroil o'g'li  ⏩ @ShuhratX95")


@dp.message_handler(Command(commands="statistika", prefixes="!"))
async def stat_admin(message: types.Message):
    id = str(message.from_user.id)
    msg = ''
    for res in db.select_all_info():
        msg += f"{res[0]} {res[1]}\n"
    if id in list(ADMINS):
        # print("admin")
        await message.answer(text=msg)
    else:
        print("no")
        await message.answer(text=message.text)


@dp.message_handler(text_contains="Taklif")
async def offer(message: types.Message):
    await message.answer(text="Taklifingizni yozing")
    await Offer.offer.set()


@dp.message_handler(state=Offer.offer)
async def offer_send(message: types.Message, state: FSMContext):
    txt = message.text
    if txt == "Katalog" or txt == "Shikoyat" or txt == "Supervisor bn bog'lanish":
        await state.finish()
        await message.answer("Menyudan tanlang", reply_markup=menu)
    else:
        offer = f"Mijozdan taklif: \n{message.text}"
        await message.answer("Taklifingiz yetkazildi!")

        for admin in ADMINS:
            await bot.send_message(chat_id=admin, text=offer)
        await state.finish()


@dp.callback_query_handler(state=MarketData.region)
async def answer_region(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    region = call.data
    await state.update_data(
                {"region": region}
            )
    await call.message.answer("Manzilingizni kiriting")

         # await PersonalData.email.set()
    await MarketData.next()
    # print(region)


@dp.message_handler(state=MarketData.region)
async def answer_region(message: types.Message, state: FSMContext):
    txt = message.text
    if txt == "Katalog" or txt == "Shikoyat" or txt == "Supervisor bn bog'lanish":
        await state.finish()
        await message.answer("Menyudan tanlang", reply_markup=menu)
    else:
        await message.answer("Menyudan tanlang", reply_markup=menu)

#     region = message.text
#
#     await state.update_data(
#         {"region": region}
#     )
#
#     await message.answer("Manzilingizni kiriting")
#
#     # await PersonalData.email.set()
#     await MarketData.next()

@dp.message_handler(state=MarketData.address)
async def answer_address(message: types.Message, state: FSMContext):
    address = message.text
    if address == "Katalog" or address == "Shikoyat" or address == "Supervisor bn bog'lanish":
        await state.finish()
        await message.answer("Menyudan tanlang", reply_markup=menu)
    else:
        await state.update_data(
            {"address": address}
        )

        await message.answer("Shikoyatni yuboring")

        await MarketData.next()


@dp.message_handler(state=MarketData.compl)
async def answer_compl(message: types.Message, state: FSMContext):
    compl = message.text
    if compl == "Katalog" or compl == "Shikoyat" or compl == "Supervisor bn bog'lanish":
        await state.finish()
        await message.answer("Menyudan tanlang", reply_markup=menu)
    else:
        await state.update_data(
            {"compl": compl}
        )

        await message.answer("Telefon raqamini +998********* formatida yuboring")

        await MarketData.next()


@dp.message_handler(state=MarketData.phone)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text
    if phone == "Katalog" or phone == "Shikoyat" or phone == "Supervisor bn bog'lanish":
        await state.finish()
        await message.answer("Menyudan tanlang", reply_markup=menu)
    else:
        if len(phone) != 13:
            await message.answer("Telefon raqamini +998********* formatida yuboring")
            await MarketData.phone.set()
        else:
            await state.update_data(
                {"phone": phone}
            )

            await message.answer("Lokatsiya yuboring")

            await MarketData.next()


@dp.message_handler(state=MarketData.location)
async def answer_location(message: types.Message, state: FSMContext):
    phone = message.text
    if phone == "Katalog" or phone == "Shikoyat" or phone == "Supervisor bn bog'lanish":
        await state.finish()
        await message.answer("Menyudan tanlang", reply_markup=menu)
    else:
        await message.answer("Menyudan tanlang", reply_markup=menu)


@dp.message_handler(content_types='location', state=MarketData.location)
async def answer_location(message: types.Message, state: FSMContext):
    location = message.location

    await state.update_data(
        {"location": location}
    )
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    region = data.get("region")
    address = data.get("address")
    compl = data.get("compl")
    phone = data.get("phone")
    db.add_info(region=region, phone=phone)
    msg = "Ma`lumotlar qabul qilindi.\nTez orada siz bilan bog'lanishadi 😊"

    await message.answer(msg)


    # State dan chiqaramiz
    # 1-variant
    complain = f"<b>YANGI SHIKOYAT</b>\n<b>Tuman:</b> {region}\n<b>Manzil:</b> {address}\n<b>Shikoyat:</b> {compl}\n<b>Telefon:</b> {phone}\n<b>Lokastiyasi</b> ⬇️⬇️⬇️"
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=complain, parse_mode='HTML')
        await bot.send_location(chat_id=admin, latitude=location.latitude, longitude=location.longitude)
    await state.finish()
    # 2-variant

    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)
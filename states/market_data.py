from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class MarketData(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    region = State() # tuman
    address = State() # manzil
    compl = State() # shikoyat
    phone = State() # telefon
    location = State() # lokatsiya

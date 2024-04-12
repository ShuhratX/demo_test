from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Katalog"),
            KeyboardButton(text="Shikoyat")
        ],
        [
            KeyboardButton(text="Taklif"),
            KeyboardButton(text="Supervisor bn bog'lanish"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
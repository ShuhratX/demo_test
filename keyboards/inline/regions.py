from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


REGIONS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="BEKTEMIR", callback_data="BEKTEMIR"),
            InlineKeyboardButton(text="MIROBOD", callback_data="MIROBOD"),
            InlineKeyboardButton(text="MIRZO ULUG'BEK", callback_data="MIRZO ULUG'BEK")
        ],
        [
            InlineKeyboardButton(text="OLMAZOR", callback_data="OLMAZOR"),
            InlineKeyboardButton(text="SERGELI", callback_data="SERGELI"),
            InlineKeyboardButton(text="UCHTEPA", callback_data="UCHTEPA")
        ],
        [
            InlineKeyboardButton(text="YAKKASAROY", callback_data="YAKKASAROY"),
            InlineKeyboardButton(text="YANGI HAYOT", callback_data="YANGI HAYOT"),
            InlineKeyboardButton(text="YASHNOBOD", callback_data="YASHNOBOD")
        ],
        [
            InlineKeyboardButton(text="YUNUSOBOD", callback_data="YUNUSOBOD"),
            InlineKeyboardButton(text="SHAYXONTOHUR", callback_data="SHAYXONTOHUR"),
            InlineKeyboardButton(text="CHILONZOR", callback_data="CHILONZOR")
        ],
        [
            InlineKeyboardButton(text="BO'STONLIQ", callback_data="BO'STONLIQ"),
            InlineKeyboardButton(text="OHANGARON", callback_data="OHANGARON"),
            InlineKeyboardButton(text="KELES", callback_data="KELES")
        ],
        [
            InlineKeyboardButton(text="QIBRAY", callback_data="QIBRAY"),
            InlineKeyboardButton(text="YANGIYO'L", callback_data="YANGIYO'L"),
            InlineKeyboardButton(text="CHIRCHIQ", callback_data="CHIRCHIQ"),
            InlineKeyboardButton(text="ZANGIOTA", callback_data="ZANGIOTA")
        ]
    ]
)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

KATALOG_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mega tuzli 200gr", callback_data="mega_1_Mega tuzli 200gr"),
            InlineKeyboardButton(text="Mega tuzsiz 200gr", callback_data="mega_2_Mega tuzsiz 200gr"),
        ],
        [
            InlineKeyboardButton(text="Mega tuzli 100gr", callback_data="mega_3_Mega tuzli 100gr"),
            InlineKeyboardButton(text="Mega tuzsiz 100gr", callback_data="mega_4_Mega tuzsiz 100gr"),
        ],
        [
            InlineKeyboardButton(text="Mega tuzli 75gr", callback_data="mega_5_Mega tuzli 75gr"),
            InlineKeyboardButton(text="Mega tuzsiz 75gr", callback_data="mega_6_Mega tuzsiz 75gr"),
        ],
        [
            InlineKeyboardButton(text="Mega oq tuzli 180gr", callback_data="mega_7_Mega oq 180gr"),
            InlineKeyboardButton(text="Mega oq tuzli 100gr", callback_data="mega_8_Mega oq 100gr"),
        ],
        [
            InlineKeyboardButton(text="Mega tuzli 3kg", callback_data="mega_11_Mega tuzli 3kg"),
            InlineKeyboardButton(text="Mega tuzsiz 2kg", callback_data="mega_12_Mega tuzsiz 2kg"),
        ],
        [
            InlineKeyboardButton(text="Keyingi", callback_data="next"),
        ]
    ]
)

KATALOG_2 = InlineKeyboardMarkup(

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Qurt 30gr", callback_data="mega_13_Qurt 30gr"),
            InlineKeyboardButton(text="Qurt  46gr", callback_data="mega_14_Qurt  46gr"),
        ],
        [
            InlineKeyboardButton(text="Qurt dona", callback_data="mega_15_Qurt dona"),
            InlineKeyboardButton(text="Xandon pista 30gr", callback_data="mega_16_Xandon pista 30gr"),
        ],
        [
            InlineKeyboardButton(text="Bodom mag'zi 40gr", callback_data="mega_17_Bodom mag'zi 40gr"),
            InlineKeyboardButton(text="Yeryong'oq 50gr", callback_data="mega_18_Yeryong'oq 50gr"),
        ],
        [
            InlineKeyboardButton(text="Qovoq tuzli 50gr", callback_data="mega_9_Qovoq tuzli 50gr"),
            InlineKeyboardButton(text="Qovoq tuzsiz 50gr", callback_data="mega_10_Qovoq tuzsiz 50gr"),
        ],
        [
            InlineKeyboardButton(text="Gaje 30gr", callback_data="mega_19_Gaje 30gr"),
        ],
        [
            InlineKeyboardButton(text="Orqaga", callback_data="prev"),
        ]
    ]
)

CANCEL = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Orqaga", callback_data="cancel"),
            ],
        ]
    )
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

rayonlar_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yunusobod"),
            KeyboardButton(text="Chilonzor"),
        ]
    ],
    resize_keyboard=True
)

yunusobod_hotels_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Radisson"),
            KeyboardButton(text="International"),
        ]
    ],
    resize_keyboard=True
)
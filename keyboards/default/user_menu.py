from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager


user_order_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳ WAITING"),
            KeyboardButton(text="✅ ACCEPTED")
        ],
        [
            KeyboardButton(text="📊 Statistics"),
            KeyboardButton(text="❌ CANCELED")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ],
    ], resize_keyboard=True
)

user_main_menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ], resize_keyboard=True
)

stickers_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Nike 👟"),
            KeyboardButton(text="Adidas 👟")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ],resize_keyboard=True
)


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager

admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Boots 👟"),
            KeyboardButton(text="Orders 🛍"),
        ],
        [
            KeyboardButton(text="Contact 📞"),
            KeyboardButton(text="Profile 👤"),
        ]
    ], resize_keyboard=True
)

admin_order_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Waiting ⏳"),
            KeyboardButton(text="Accepted ✅")
        ],
        [
            KeyboardButton(text="Statistics 📊"),
            KeyboardButton(text="Canceled ❌")
        ],
        [
            KeyboardButton(text="Back ⬅️")
        ],
    ], resize_keyboard=True
)

admin_back_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back ⬅️")
        ]
    ], resize_keyboard=True
)


async def admin_boots_menu_def():
    stickers = db_manager.get_all_boots()
    admin_stickers_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    back = KeyboardButton(text="Back ⬅️")
    admin_stickers_menu.insert(back)

    for sticker in stickers:
        keyboard = KeyboardButton(text=sticker[1])
        admin_stickers_menu.insert(keyboard)

    return admin_stickers_menu



admin_nike_boots = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Nike Phantom"),
            KeyboardButton(text="Nike Air Zoom"),
        ],
        [
            KeyboardButton(text="Back ⬅️")
        ]
    ], resize_keyboard=True
)
admin_back_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back ⬅️")
        ]
    ], resize_keyboard=True
)


admin_Adidas_boots = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Adidas Predator"),
            KeyboardButton(text="Adidas X"),
        ],
        [
            KeyboardButton(text="Back ⬅️")
        ]
    ], resize_keyboard=True
)
admin_back_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back ⬅️")
        ]
    ], resize_keyboard=True
)
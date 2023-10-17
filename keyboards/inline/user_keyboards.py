from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def user_product_buy_def(quantity, total):
    user_product_buy = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➖", callback_data="minus_product"),
                InlineKeyboardButton(text=f"{quantity}/{total}", callback_data="popo"),
                InlineKeyboardButton(text="➕", callback_data="plus_product"),
            ],
            [
                InlineKeyboardButton(text="🛍 Savatni ko'rish", callback_data="show_basket"),
            ]
        ]
    )
    return user_product_buy


user_profile_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ism", callback_data="change_full_name"),
            InlineKeyboardButton(text="Raqam", callback_data="change_phone_number"),
        ],
        [
            InlineKeyboardButton(text="Modme ID", callback_data="change_modme_id"),
            InlineKeyboardButton(text="Guruh raqam", callback_data="change_group_number"),
        ],
        [
            InlineKeyboardButton(text="Guruh turi", callback_data="change_group_type"),
            InlineKeyboardButton(text="ID ni olish", callback_data="get_user_id"),
        ]
    ]
)

user_basket_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛍 Zakaz berish", callback_data="order_basket"),
            InlineKeyboardButton(text="🧹 Savatni tozalash", callback_data="clear_basket"),
        ]
    ]
)

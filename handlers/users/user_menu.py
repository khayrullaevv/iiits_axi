from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import InputFile
from data.config import ADMINS
from handlers.users.backs import stickers_oaoa_menu
from keyboards.inline.admin_keyboards import admin_order_decision_def
from keyboards.inline.user_keyboards import user_product_buy_def, user_basket_menu
from keyboards.default.user_menu import stickers_menu
from loader import dp, db_manager
from utils.random_number import get_random_id


@dp.message_handler(text="Boots 👟")
async def stickers_menu_handler(message: types.Message):
    text = "Quyidagi butsilardan birini tanlang."
    await message.answer(text=text, reply_markup=stickers_menu)

@dp.message_handler(text="Adidas Predator")
async def cats_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Predator") if basket.get("Predator") else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Predator",
        "price": 40
    })
    photo = ""
    text = "😻 Nike\Butsilar to'plami Adidas Nike, 10 dona\nNarxi: 40-50$"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))



@dp.callback_query_handler(text="show_basket", state="user-stickers-state")
async def show_product_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket')
    if basket:
        text = "Sizning savatingizda quyidagi mahsulotlar bor: \n\n"
        counter = 1
        total = 0
        for product in basket.values():
            text += f"<i><b>{counter}) {product['name']}\t| {product['quantity']} ta " \
                    f"\t| {product['price']} so'm\t| {product['total']} so'm\n</b></i>"
            counter += 1
            total += product['total']
        text += f"\nJami: {total} so'm"

        await call.message.answer(text=text, reply_markup=user_basket_menu)
    else:
        text = "Sizning savatingizda hech narsa mavjud emas. ❗️"
        await call.answer(text=text, show_alert=True)


@dp.callback_query_handler(text="clear_basket", state="user-stickers-state")
async def clear_basket_handler(call: CallbackQuery, state: FSMContext):
    await state.update_data({
        "basket": dict()
    })
    popup = "Savat tozalandi ❗️"
    await call.answer(text=popup, show_alert=True)
    text = "Sizning savatingizda quyidagi mahsulotlar bor: "
    await call.message.edit_text(text=text)


@dp.callback_query_handler(text="order_basket", state="user-stickers-state")
async def order_basket_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket')
    user = db_manager.get_user(call.message)
    order_id = get_random_id()
    if basket and user:
        text = "Sizning zakazingiz quyidagi ko'rinishda: \n"
        text += f"""
ID: {order_id}
FI: {user[2]}
TEL: {user[3]}
SANA: {call.message.date}
STATUS: WAITING

"""
        counter = 1
        total = 0
        for product in basket.values():
            text += f"<i><b>{counter}) {product['name']}\t| {product['quantity']} ta " \
                    f"\t| {product['price']} so'm\t| {product['total']} so'm\n</b></i>"
            counter += 1
            total += product['total']
        text += f"\nJami: {total} so'm"

        await state.update_data({
            "basket": dict()
        })
        new_order = db_manager.append_order(call.message, basket, order_id)
        if not new_order:
            admin_text = "Zakazlarni bazaga qo'shish joyida xatolik chiqdi"
            await dp.bot.send_message(text=admin_text, chat_id=ADMINS[0])

        await dp.bot.send_message(chat_id=ADMINS[0], text=text,
                                  reply_markup=await admin_order_decision_def(order_id, call.message.chat.id))
        await call.message.answer(text=text)
    else:
        text = "Sizning savatingizda hech narsa mavjud emas. ❗️"
        await call.answer(text=text, show_alert=True)
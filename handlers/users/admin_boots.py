from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin_menu import admin_back_main_menu, admin_nike_boots, admin_Adidas_boots

from loader import dp, db_manager

@dp.message_handler(text="Nike 👟")
async def admin_order_handler(message: types.Message, state: FSMContext):
    await state.set_state('admin-boots-state')
    text = "Mahsulotlar manyusiga xush kelibsiz"
    await message.answer(text=text, reply_markup=admin_nike_boots)

@dp.message_handler(text="Adidas 👟")
async def stickers_menu_handler(message: types.Message):
    text = "Quyidagi butsilardan birini tanlang."
    await message.answer(text=text, reply_markup=admin_Adidas_boots)
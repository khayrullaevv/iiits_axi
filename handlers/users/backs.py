from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin_menu import admin_main_menu
from loader import dp


@dp.message_handler(text="⬅️ Back", state="*")
async def stickers_menu(message: types.Message, state: FSMContext):
    text = "Welcom to main menu"
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()


@dp.message_handler(text="Back ⬅️", chat_id=ADMINS, state="*")
async def boots_oaoa_menu(message: types.Message, state: FSMContext):
    text = "Welcom to main menu"
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()

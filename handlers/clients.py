from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.db import get_client_apps_by_os

router = Router()

@router.message(F.text == "📲 دانلود کلاینت‌ها")
async def choose_os(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📱 اندروید", callback_data="clients_android")],
        [InlineKeyboardButton(text="💻 ویندوز", callback_data="clients_windows")],
        [InlineKeyboardButton(text="🍏 آی‌او‌اس", callback_data="clients_ios")],
    ])
    await message.answer("📥 سیستم عاملتو انتخاب کن:", reply_markup=kb)

@router.callback_query(F.data.startswith("clients_"))
async def show_clients(callback: CallbackQuery):
    os_type = callback.data.split("_")[1]
    apps = get_client_apps_by_os(os_type)
    if not apps:
        await callback.message.edit_text("❌ هنوز هیچ کلاینتی برای این سیستم ثبت نشده.")
        return
    text = f"📲 کلاینت‌های قابل دانلود برای {os_type.upper()}:\n\n"
    for name, url in apps:
        text += f"🔸 [{name}]({url})\n"
    await callback.message.edit_text(text, parse_mode="Markdown")

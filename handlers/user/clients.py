from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.db import get_clients_by_type

router = Router()

@router.message(F.text == "📱 لیست کلاینت‌ها")
async def choose_client_type(message: Message):
    buttons = [
        [InlineKeyboardButton(text="📱 اندروید", callback_data="client_Android")],
        [InlineKeyboardButton(text="💻 ویندوز", callback_data="client_Windows")],
        [InlineKeyboardButton(text="🍏 iOS", callback_data="client_iOS")],
        [InlineKeyboardButton(text="🍎 MacOS", callback_data="client_Mac")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer("📂 نوع سیستم‌عامل رو انتخاب کن:", reply_markup=markup)

@router.callback_query(F.data.startswith("client_"))
async def show_clients(callback_query):
    _, client_type = callback_query.data.split("_", 1)
    clients = get_clients_by_type(client_type)

    if not clients:
        await callback_query.message.answer("⛔ کلاینتی برای این نوع وجود نداره.")
        return

    text = f"📦 کلاینت‌های {client_type}:\n\n"
    for name, link in clients:
        text += f"🔸 {name}\n🔗 {link}\n\n"
    
    await callback_query.message.answer(text)

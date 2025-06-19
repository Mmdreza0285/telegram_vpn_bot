from aiogram import Router, F
from aiogram.types import Message
from database.db import get_bot_stats

router = Router()

@router.message(F.text == "📊 آمار ربات")
async def show_stats(message: Message):
    users, servers, refs = get_bot_stats()
    text = f"""
📊 آمار کلی ربات:

👥 کاربران: {users}
🌐 سرورها: {servers}
🔁 رفرال‌ها: {refs}
"""
    await message.answer(text)

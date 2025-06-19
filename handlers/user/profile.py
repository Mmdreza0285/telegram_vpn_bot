from aiogram import Router, F
from aiogram.types import Message
from database.db import get_user_profile

router = Router()

@router.message(F.text == "👤 وضعیت حساب من")
async def profile(message: Message):
    data = get_user_profile(message.from_user.id)
    if not data:
        await message.answer("⛔ اطلاعاتی یافت نشد.")
        return
    
    joined, refs, level, donated = data
    text = f"""
📍 پروفایل شما:

🆔 آی‌دی: {message.from_user.id}
📅 تاریخ عضویت: {joined}
👥 رفرال‌ها: {refs}
🎖️ سطح کاربر: {level}
🎁 کانفیگ‌های اهدا شده: {donated}
"""
    await message.answer(text)

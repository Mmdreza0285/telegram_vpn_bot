from aiogram import Router, F
from aiogram.types import Message
from database.db import get_bot_stats, get_user_info

router = Router()

@router.message(F.text == "📊 آمار ربات")
async def bot_stats(message: Message):
    user_id = message.from_user.id
    info = get_user_info(user_id)
    if not info or info["role"] != "admin":
        await message.answer("⛔ فقط ادمین می‌تونه آمار ببینه.")
        return

    stats = get_bot_stats()
    text = f"""📊 آمار کلی ربات:

👤 تعداد کل کاربران: {stats["users"]}
🧩 تعداد کانفیگ‌ها: {stats["configs"]}
👥 رفرال‌های موفق: {stats["referrals"]}
📂 سرورهای ثبت‌شده: {stats["servers"]}
🕓 کاربران ۲۴ ساعت اخیر: {stats["recent_users"]}
"""
    await message.answer(text)

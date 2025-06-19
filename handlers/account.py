from aiogram import Router, F
from aiogram.types import Message
from database.db import get_user_info, get_user_config_count, get_user_referral_count

router = Router()

@router.message(F.text == "👤 حساب کاربری من")
async def account_info(message: Message):
    user_id = message.from_user.id
    info = get_user_info(user_id)
    if not info:
        await message.answer("❌ مشکلی در دریافت اطلاعات پیش اومده.")
        return

    configs = get_user_config_count(user_id)
    referrals = get_user_referral_count(user_id)

    text = f"""👤 وضعیت حساب شما:

🆔 آیدی عددی: `{user_id}`
🎭 نقش: {info["role"]}
📅 تاریخ عضویت: {info["join_date"]}
📤 کانفیگ‌های اهدا شده: {configs}
👥 تعداد دعوت‌شدگان: {referrals}
"""
    await message.answer(text, parse_mode="Markdown")

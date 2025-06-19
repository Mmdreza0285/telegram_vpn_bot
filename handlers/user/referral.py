# handlers/user/referral.py

from aiogram import Router, F
from aiogram.types import Message
from database.db import get_referral_count

router = Router()

@router.message(F.text == "👥 دعوت دوستان")
async def show_referral(message: Message):
    count = get_referral_count(message.from_user.id)
    link = f"https://t.me/{(await message.bot.get_me()).username}?start={message.from_user.id}"

    await message.answer(
        f"🎁 با دعوت دوستان کانفیگ هدیه بگیر!\n\n"
        f"🔗 لینک دعوت اختصاصی شما:\n{link}\n\n"
        f"👤 تعداد افرادی که دعوت کردی: {count}"
    )

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database.db import add_user, count_referrals, get_user_by_id
from config import BOT_USERNAME

router = Router()

@router.message(Command("start"))
async def handle_start(message: Message):
    user_id = message.from_user.id
    args = message.text.split()
    ref_id = int(args[1]) if len(args) > 1 and args[1].isdigit() else None

    user = get_user_by_id(user_id)
    if not user:
        add_user(user_id, ref_id)

    await message.answer("🎉 به ربات خوش اومدی!\nاز منوی زیر استفاده کن.")

@router.message(lambda m: m.text == "📣 لینک دعوت من")
async def my_referral(message: Message):
    link = f"https://t.me/{BOT_USERNAME}?start={message.from_user.id}"
    count = count_referrals(message.from_user.id)
    await message.answer(f"""🔗 لینک دعوت شما:
{link}

👥 تعداد دعوت‌های شما: {count} نفر
""")

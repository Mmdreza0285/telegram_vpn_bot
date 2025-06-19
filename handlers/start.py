from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import db

async def on_start(message: Message, bot):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    ref_by = 0

    # بررسی عضویت در کانال (مثلاً @shadoowvpnn)
    channels = ["@shadoowvpnn"]
    for channel in channels:
        try:
            member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ['creator', 'administrator', 'member']:
                await message.answer(f"⛔️ برای استفاده از ربات ابتدا عضو {channel} شوید.")
                return
        except:
            await message.answer(f"⛔️ برای استفاده از ربات ابتدا عضو {channel} شوید.")
            return

    # ذخیره در دیتابیس
    db.save_user(user_id, username, first_name, ref_by)

    # منو اصلی
    from keyboards.default import main_menu
    await message.answer(f"سلام {first_name} 👋 به ربات وی‌پی‌ان خوش اومدی!", reply_markup=main_menu())

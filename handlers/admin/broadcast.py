from aiogram import Router, F
from aiogram.types import Message
from config import ADMINS
from database.db import get_all_users
from asyncio import sleep

router = Router()

@router.message(F.text == "📢 پیام همگانی")
async def ask_broadcast(message: Message):
    if message.from_user.id not in ADMINS:
        return
    await message.answer("📝 پیامتو بفرست:")

@router.message()
async def do_broadcast(message: Message):
    if message.from_user.id not in ADMINS:
        return
    
    users = get_all_users()
    sent = 0
    for user_id in users:
        try:
            await message.bot.send_message(user_id, message.text)
            sent += 1
            await sleep(0.05)
        except:
            continue
    await message.answer(f"📤 ارسال شد به {sent} نفر.")

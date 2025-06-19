from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from database.db import get_all_users
from config import ADMINS

router = Router()
broadcasting_admin = {}

@router.message(Command("broadcast"), F.from_user.id.in_(ADMINS))
async def broadcast_start(msg: Message):
    await msg.answer("پیام همگانی خود را ارسال کنید.")
    broadcasting_admin[msg.from_user.id] = True

@router.message(F.from_user.id.in_(ADMINS))
async def broadcast_message(msg: Message):
    if broadcasting_admin.get(msg.from_user.id):
        users = await get_all_users()
        for user in users:
            try:
                await msg.bot.send_message(chat_id=user["user_id"], text=msg.text)
            except:
                continue
        await msg.answer("✅ پیام برای همه کاربران ارسال شد.")
        broadcasting_admin[msg.from_user.id] = False

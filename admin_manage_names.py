from aiogram import Router, F
from aiogram.types import Message
from database.db import update_all_server_names
from config import ADMINS

router = Router()

@router.message(F.text.startswith("📝 تغییر نام سرورها "), F.from_user.id.in_(ADMINS))
async def change_names(msg: Message):
    new_name = msg.text.replace("📝 تغییر نام سرورها ", "")
    await update_all_server_names(new_name)
    await msg.answer(f"✅ تمام نام‌ها به «{new_name}» تغییر یافتند.")

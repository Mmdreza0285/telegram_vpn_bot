# handlers/user/start.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.user_menu import user_main_menu
from database.db import create_user_if_not_exists

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await create_user_if_not_exists(
        user_id=message.from_user.id,
        username=message.from_user.username or "",
        full_name=message.from_user.full_name,
        referral_by=None  # اگر از لینک رفرال وارد شد، بعداً می‌گیریم
    )

    await message.answer(
        f"سلام {message.from_user.full_name} 👋\n"
        "به ربات فیلترشکن خوش اومدی!\n"
        "از منوی زیر یکی از گزینه‌ها رو انتخاب کن:",
        reply_markup=user_main_menu()
    )

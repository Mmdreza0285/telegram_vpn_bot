from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

from config import ADMINS

router = Router()

@router.message(Command("admin"))
async def admin_panel(msg: Message):
    if msg.from_user.id not in ADMINS:
        return
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="📤 ارسال پیام همگانی")],
        [KeyboardButton(text="📥 ارسال خودکار به کانال")],
        [KeyboardButton(text="📝 تغییر نام سرورها test-name")],
        [KeyboardButton(text="⬅ بازگشت به منوی اصلی")]
    ], resize_keyboard=True)
    await msg.answer("پنل مدیریتی فعال شد.", reply_markup=keyboard)

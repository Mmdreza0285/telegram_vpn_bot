from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import ADMINS

router = Router()

@router.message(F.text == "/admin")
async def admin_panel(message: Message):
    if message.from_user.id not in ADMINS:
        return

    buttons = [
        [KeyboardButton(text="📊 آمار ربات"), KeyboardButton(text="📢 پیام همگانی")],
        [KeyboardButton(text="➕ افزودن ادمین"), KeyboardButton(text="🔄 تغییر کانال عضویت")],
        [KeyboardButton(text="➕ افزودن کلاینت"), KeyboardButton(text="📂 مدیریت سرورها")],
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("🎛️ به پنل مدیریت خوش اومدی", reply_markup=markup)

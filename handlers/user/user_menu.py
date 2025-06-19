from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def user_start(msg: Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="🎁 دریافت سرور رایگان")],
        [KeyboardButton(text="🎯 ارسال کانفیگ شخصی")],
        [KeyboardButton(text="👥 رفرال من"), KeyboardButton(text="📊 وضعیت حساب")],
        [KeyboardButton(text="🧩 لیست کلاینت ها"), KeyboardButton(text="📞 ارتباط با پشتیبانی")]
    ], resize_keyboard=True)
    await msg.answer("به منوی اصلی خوش آمدید!", reply_markup=keyboard)

# keyboards/user_menu.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def user_main_menu():
    buttons = [
        [KeyboardButton(text="📡 دریافت کانفیگ رایگان")],
        [KeyboardButton(text="📤 اهدای کانفیگ"), KeyboardButton(text="🎁 رفرال")],
        [KeyboardButton(text="📥 کلاینت‌ها"), KeyboardButton(text="📈 وضعیت حساب")],
        [KeyboardButton(text="📬 ارتباط با پشتیبانی")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        input_field_placeholder="یکی از گزینه‌ها رو انتخاب کن"
    )

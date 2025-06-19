from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def user_main_menu():
    buttons = [
        [KeyboardButton("📡 دریافت کانفیگ رایگان")],
        [KeyboardButton("📤 اهدای کانفیگ"), KeyboardButton("🎁 رفرال")],
        [KeyboardButton("📥 کلاینت‌ها"), KeyboardButton("📈 وضعیت حساب")],
        [KeyboardButton("📬 ارتباط با پشتیبانی")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

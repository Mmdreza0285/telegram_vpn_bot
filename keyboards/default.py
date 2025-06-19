from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🎁 دریافت سرور رایگان"))
    kb.add(KeyboardButton("🧾 ارسال کانفیگ (اهدایی)"))
    kb.add(KeyboardButton("📈 وضعیت اکانت"))
    kb.add(KeyboardButton("🎯 سیستم رفرال"))
    kb.add(KeyboardButton("📲 دانلود کلاینت‌ها"))
    kb.add(KeyboardButton("🛠 پنل مدیریت"))
    return kb

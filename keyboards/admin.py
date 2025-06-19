from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_menu():
    buttons = [
        [KeyboardButton("📊 آمار ربات"), KeyboardButton("📬 پیام همگانی")],
        [KeyboardButton("🧑‍💼 مدیریت ادمین‌ها"), KeyboardButton("🔗 تنظیم کانال عضویت")],
        [KeyboardButton("📥 مدیریت سرورها")],
        [KeyboardButton("🎨 تنظیم پیام‌ها"), KeyboardButton("📲 مدیریت کلاینت‌ها")],
        [KeyboardButton("⏱️ زمان‌بندی ارسال سرورها")],
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

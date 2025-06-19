from aiogram import types
from aiogram.dispatcher import Dispatcher
from database import db

ADMIN_IDS = [123456789]  # آیدی ادمین‌ها

async def admin_panel(message: types.Message):
    if message.from_user.id not in ADMIN_IDS:
        return
    user_count = db.get_user_count()
    await message.reply(f"🔧 پنل مدیریت\n👥 تعداد کل کاربران: {user_count}")

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_panel, lambda m: m.text == "🛠 پنل مدیریت")

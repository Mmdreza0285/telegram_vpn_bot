from aiogram import types
from aiogram.dispatcher import Dispatcher
from database import db

async def handle_account_status(message: types.Message):
    count = db.get_referral_count(message.from_user.id)
    await message.reply(f"📊 شما تا الان {count} نفر را به ربات دعوت کرده‌اید!")

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_account_status, lambda m: m.text == "📈 وضعیت اکانت")

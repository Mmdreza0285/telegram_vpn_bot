from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import ADMINS
from database.db import set_text_config, get_text_config

router = Router()

texts_keys = {
    "start_text": "✏️ تغییر پیام شروع",
    "menu_buttons": "🎛️ تغییر دکمه‌های منو",
    "config_submit_text": "📦 تغییر پیام ارسال کانفیگ"
}

@router.message(F.text.in_(list(texts_keys.values())))
async def change_text_prompt(message: Message):
    if message.from_user.id not in ADMINS:
        return
    for key, label in texts_keys.items():
        if message.text == label:
            await message.answer(f"📝 متن جدید برای {label} رو بفرست:")
            await message.bot.set_state(user_id=message.from_user.id, state=key)
            return

@router.message()
async def save_custom_text(message: Message):
    state = await message.bot.get_state(user_id=message.from_user.id)
    if state in texts_keys:
        set_text_config(state, message.text)
        await message.answer("✅ متن با موفقیت ذخیره شد.")
        await message.bot.set_state(user_id=message.from_user.id, state=None)

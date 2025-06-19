from aiogram import Router, F
from aiogram.types import Message
from database.db import get_user_info, add_channel, remove_channel, get_channels

router = Router()

@router.message(F.text == "📢 مدیریت عضویت اجباری")
async def show_join_channels(message: Message):
    info = get_user_info(message.from_user.id)
    if not info or info["role"] != "admin":
        return

    channels = get_channels()
    text = "📢 لیست کانال‌های عضویت اجباری:\n" + "\n".join([f"@{c}" for c in channels]) if channels else "⛔ هنوز کانالی ثبت نشده."

    text += "\n\n➕ برای افزودن کانال بنویس:\nadd @username\n➖ برای حذف:\nremove @username"
    await message.answer(text)

@router.message(F.text.startswith("add @"))
async def add_join_channel(message: Message):
    if get_user_info(message.from_user.id)["role"] != "admin": return
    username = message.text.split(" ")[1].replace("@", "")
    add_channel(username)
    await message.answer(f"✅ کانال @{username} افزوده شد.")

@router.message(F.text.startswith("remove @"))
async def remove_join_channel(message: Message):
    if get_user_info(message.from_user.id)["role"] != "admin": return
    username = message.text.split(" ")[1].replace("@", "")
    remove_channel(username)
    await message.answer(f"❌ کانال @{username} حذف شد.")

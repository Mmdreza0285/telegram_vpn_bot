from aiogram import Router, types, F
from database.db import add_required_channel, delete_required_channel, get_required_channels

router = Router()

@router.message(F.text == "📢 مدیریت کانال‌های اجباری")
async def show_channel_menu(message: types.Message):
    channels = get_required_channels()
    text = "📋 لیست کانال‌های فعلی:\n"
    if not channels:
        text += "هیچ کانالی اضافه نشده."
    else:
        for ch in channels:
            text += f"▫️ @{ch}\n"

    text += "\n🔘 برای افزودن: `+ @channel`\n🔘 برای حذف: `- @channel`"
    await message.answer(text, parse_mode="Markdown")

@router.message(F.text.regexp(r"^[+-]\s*@[\w\d_]+$"))
async def manage_channels(message: types.Message):
    text = message.text.strip()
    action = text[0]
    channel = text[2:]

    if action == "+":
        add_required_channel(channel)
        await message.answer(f"✅ کانال @{channel} اضافه شد.")
    elif action == "-":
        delete_required_channel(channel)
        await message.answer(f"🗑 کانال @{channel} حذف شد.")

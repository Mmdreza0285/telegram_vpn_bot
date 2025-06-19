from aiogram import Router, F
from aiogram.types import Message
from config import ADMINS
from database.db import save_bulk_servers, set_auto_name
import asyncio

router = Router()

@router.message(F.text.startswith("📥 افزودن گروهی سرور"))
async def bulk_add_servers(message: Message):
    if message.from_user.id not in ADMINS:
        return
    await message.answer("📝 لیست سرورها رو بفرست (هر خط یک سرور):")

@router.message()
async def handle_server_list(message: Message):
    if message.from_user.id not in ADMINS:
        return
    
    if len(message.text.split('\n')) < 2:
        return
    
    servers = message.text.strip().split('\n')
    save_bulk_servers(servers)
    await message.answer(f"✅ {len(servers)} سرور ذخیره شد و به ترتیب ارسال می‌شن.")

@router.message(F.text.startswith("🔖 تنظیم برچسب سرور"))
async def set_label(message: Message):
    if message.from_user.id not in ADMINS:
        return
    label = message.text.replace("🔖 تنظیم برچسب سرور ", "").strip()
    set_auto_name(label)
    await message.answer(f"✅ برچسب جدید: `{label}`")

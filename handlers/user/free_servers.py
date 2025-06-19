# handlers/user/free_servers.py

from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Text
from database.db import get_protocols, get_countries_by_protocol, get_servers

router = Router()

@router.message(Text("📡 دریافت کانفیگ رایگان"))
async def choose_protocol(message: Message):
    protocols = get_protocols()
    buttons = [[KeyboardButton(text=p)] for p in protocols]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("🔰 پروتکل مورد نظر رو انتخاب کن:", reply_markup=markup)

@router.message(Text(startswith="V2Ray") | Text(startswith="VLESS") | Text(startswith="Outline") | Text(startswith="Hysteria") | Text(startswith="Reality"))
async def choose_country(message: Message):
    protocol = message.text.strip()
    countries = get_countries_by_protocol(protocol)

    if not countries:
        await message.answer("⚠️ هیچ کشوری برای این پروتکل موجود نیست.")
        return

    buttons = []
    for country, count, flag in countries:
        buttons.append([KeyboardButton(text=f"{flag} {country} ({count})")])

    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    await message.answer("🌍 کشور مورد نظر رو انتخاب کن:", reply_markup=markup)

@router.message(Text(contains="("))  # فرض: متن شبیه 🇩🇪 آلمان (3)
async def send_configs(message: Message):
    full_text = message.text
    flag = full_text[0:2]
    country = full_text[3:].split(" (")[0]

    protocol = ""  # از آخرین پیام نمی‌گیریم چون FSM نذاشتیم فعلاً

    # اینو بهینه می‌کنیم در آینده با FSM
    await message.answer("⏳ درحال دریافت کانفیگ‌ها...")

    servers = get_servers(protocol=None, country=country)  # در نسخه ساده بدون فیلتر پروتکل
    if not servers:
        await message.answer("❌ کانفیگی برای این کشور موجود نیست.")
        return

    for server in servers:
        await message.answer(f"🔗 <code>{server[4]}</code>", disable_web_page_preview=True)

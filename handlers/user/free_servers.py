# handlers/user/free_servers.py

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database.db import get_available_countries, get_configs_by_filter

router = Router()

class GetServer(StatesGroup):
    protocol = State()
    country = State()

@router.message(F.text == "🌐 دریافت سرور رایگان")
async def choose_protocol(message: Message, state: FSMContext):
    protocols = ["V2Ray", "VLESS", "Reality", "Hysteria2", "Outline"]
    buttons = [[KeyboardButton(text=p)] for p in protocols]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    await message.answer("📡 پروتکل مورد نظر رو انتخاب کن:", reply_markup=markup)
    await state.set_state(GetServer.protocol)

@router.message(GetServer.protocol)
async def choose_country(message: Message, state: FSMContext):
    protocol = message.text
    await state.update_data(protocol=protocol)

    countries = get_available_countries(protocol)
    if not countries:
        await message.answer("⛔ هیچ سروری برای این پروتکل موجود نیست.")
        await state.clear()
        return

    # ساخت دکمه‌ها با پرچم و تعداد
    buttons = [[KeyboardButton(text=f"{flag} {country} ({count})")] for flag, country, count in countries]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    await message.answer("🌍 کشور رو انتخاب کن:", reply_markup=markup)
    await state.set_state(GetServer.country)

@router.message(GetServer.country)
async def send_servers(message: Message, state: FSMContext):
    country_text = message.text
    country = country_text[3:].split('(')[0].strip()

    data = await state.get_data()
    protocol = data['protocol']

    configs = get_configs_by_filter(protocol, country)
    if not configs:
        await message.answer("❌ متأسفم، سروری پیدا نشد.")
    else:
        await message.answer(f"✅ {len(configs)} سرور موجوده:\n\n" + "\n\n".join(configs[:10]))

    await state.clear()

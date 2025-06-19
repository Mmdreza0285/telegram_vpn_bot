from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from database.db import get_server_summary, get_servers_by_category
from utils.flags import FLAGS

router = Router()

@router.message(lambda msg: msg.text == "📡 دریافت سرورها")
async def show_protocols(message: Message):
    summary = get_server_summary()
    grouped = {}

    for protocol, country, count in summary:
        if protocol not in grouped:
            grouped[protocol] = []
        grouped[protocol].append((country, count))

    for protocol, items in grouped.items():
        kb = []
        for country, count in items:
            flag = FLAGS.get(country, "")
            kb.append([InlineKeyboardButton(
                text=f"{flag} {country} ({count})",
                callback_data=f"get_{protocol}_{country}"
            )])
        
        await message.answer(f"🌐 {protocol} سرورها:", reply_markup=InlineKeyboardMarkup(inline_keyboard=kb))

@router.callback_query(lambda c: c.data.startswith("get_"))
async def show_configs(callback: types.CallbackQuery):
    _, protocol, country = callback.data.split("_", 2)
    servers = get_servers_by_category(protocol, country)
    if not servers:
        await callback.message.answer("⛔ سروری موجود نیست.")
        return
    
    for name, config in servers:
        await callback.message.answer(f"📡 {name}\n\n`{config}`", parse_mode="Markdown")
    await callback.answer()

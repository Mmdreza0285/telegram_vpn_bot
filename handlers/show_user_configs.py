from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.db import get_available_protocols, get_countries_for_protocol, get_configs_by_category

router = Router()

@router.message(F.text == "📤 کانفیگ‌های کاربران")
async def show_protocols(message: Message):
    protocols = get_available_protocols()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=p.upper(), callback_data=f"showproto_{p}")] for p in protocols
    ])
    await message.answer("🔐 پروتکل مورد نظر رو انتخاب کن:", reply_markup=kb)

@router.callback_query(F.data.startswith("showproto_"))
async def show_countries(callback: CallbackQuery):
    proto = callback.data.split("_")[1]
    countries = get_countries_for_protocol(proto)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🇨🇭 {c.upper()}", callback_data=f"showcfg_{proto}_{c}")] for c in countries
    ])
    await callback.message.edit_text(f"🌍 کشور برای پروتکل {proto.upper()} رو انتخاب کن:", reply_markup=kb)

@router.callback_query(F.data.startswith("showcfg_"))
async def show_configs(callback: CallbackQuery):
    _, proto, country = callback.data.split("_")
    configs = get_configs_by_category(proto, country)
    if not configs:
        await callback.message.edit_text("❌ کانفیگی تو این دسته‌بندی هنوز ثبت نشده.")
        return
    text = f"📤 کانفیگ‌های ثبت‌شده برای {proto.upper()} / {country.upper()}:\n\n"
    for i, cfg in enumerate(configs, start=1):
        text += f"{i}. `{cfg}`\n\n"
    await callback.message.edit_text(text[:4096], parse_mode="Markdown")

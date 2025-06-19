# handlers/user/donate_config.py

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from database.db import save_donated_config

router = Router()

# حالت‌ها
class DonateConfig(StatesGroup):
    waiting_protocol = State()
    waiting_country = State()
    waiting_config = State()

@router.message(F.text == "📤 اهدای کانفیگ")
async def start_donation(message: Message, state: FSMContext):
    protocols = ["V2Ray", "VLESS", "Hysteria2", "Reality", "Outline"]
    buttons = [[KeyboardButton(text=p)] for p in protocols]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    await message.answer("🔰 پروتکل کانفیگ رو انتخاب کن:", reply_markup=markup)
    await state.set_state(DonateConfig.waiting_protocol)

@router.message(DonateConfig.waiting_protocol)
async def choose_country(message: Message, state: FSMContext):
    await state.update_data(protocol=message.text)

    countries = ["🇩🇪 آلمان", "🇹🇷 ترکیه", "🇺🇸 آمریکا", "🇫🇷 فرانسه", "🇷🇺 روسیه", "🇬🇧 انگلیس"]
    buttons = [[KeyboardButton(text=c)] for c in countries]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

    await message.answer("🌍 کشور سرور رو انتخاب کن:", reply_markup=markup)
    await state.set_state(DonateConfig.waiting_country)

@router.message(DonateConfig.waiting_country)
async def get_config(message: Message, state: FSMContext):
    country_text = message.text
    country = country_text[3:]  # حذف ایموجی پرچم
    flag = country_text[:2]

    await state.update_data(country=country, flag=flag)

    await message.answer("🔗 لطفاً کانفیگ (کد) رو ارسال کن:")
    await state.set_state(DonateConfig.waiting_config)

@router.message(DonateConfig.waiting_config)
async def save_config(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = message.from_user.id

    save_donated_config(
        user_id=user_id,
        protocol=data["protocol"],
        country=data["country"],
        flag=data["flag"],
        config_text=message.text
    )

    await message.answer("✅ کانفیگ شما دریافت شد و پس از تایید ادمین منتشر می‌شود. ممنون از همکاری شما 💖")
    await state.clear()

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import add_server

router = Router()

class AddServerState(StatesGroup):
    protocol = State()
    country = State()
    name = State()
    config = State()

@router.message(F.text == "➕ افزودن سرور")
async def start_add_server(message: types.Message, state: FSMContext):
    await message.answer("📡 پروتکل سرور رو وارد کن:\n(مثلاً: V2Ray, Outline, Hysteria, VLESS)")
    await state.set_state(AddServerState.protocol)

@router.message(AddServerState.protocol)
async def get_protocol(message: types.Message, state: FSMContext):
    await state.update_data(protocol=message.text)
    await message.answer("🌍 کشور سرور رو وارد کن:\n(مثلاً: ایران، ترکیه، آمریکا...)")
    await state.set_state(AddServerState.country)

@router.message(AddServerState.country)
async def get_country(message: types.Message, state: FSMContext):
    await state.update_data(country=message.text)
    await message.answer("📛 اسم نمایشی سرور رو وارد کن:")
    await state.set_state(AddServerState.name)

@router.message(AddServerState.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("🔐 کانفیگ رو ارسال کن:")
    await state.set_state(AddServerState.config)

@router.message(AddServerState.config)
async def get_config(message: types.Message, state: FSMContext):
    data = await state.get_data()
    protocol = data['protocol']
    country = data['country']
    name = data['name']
    config = message.text
    added_by = message.from_user.id

    add_server(protocol, country, name, config, added_by)
    await message.answer("✅ سرور با موفقیت ذخیره شد!")
    await state.clear()

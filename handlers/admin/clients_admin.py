from aiogram import Router, F
from aiogram.types import Message
from database.db import add_client, delete_client
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

class AddClient(StatesGroup):
    type = State()
    name = State()
    link = State()

@router.message(F.text == "➕ افزودن کلاینت")
async def start_add_client(message: Message, state: FSMContext):
    await message.answer("🔸 نوع کلاینت؟ (Android, Windows, iOS, Mac)")
    await state.set_state(AddClient.type)

@router.message(AddClient.type)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(type=message.text)
    await message.answer("📛 اسم کلاینت؟")
    await state.set_state(AddClient.name)

@router.message(AddClient.name)
async def add_link(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("🔗 لینک دانلود کلاینت:")
    await state.set_state(AddClient.link)

@router.message(AddClient.link)
async def save_client(message: Message, state: FSMContext):
    data = await state.get_data()
    add_client(data['type'], data['name'], message.text)
    await message.answer("✅ کلاینت با موفقیت افزوده شد!")
    await state.clear()

@router.message(F.text.startswith("❌ حذف کلاینت"))
async def remove_client(message: Message):
    parts = message.text.split(" ", 2)
    if len(parts) < 3:
        await message.answer("❗ لطفاً به فرمت صحیح بنویس: ❌ حذف کلاینت Windows V2RayNG")
        return
    _, client_type, name = parts
    delete_client(client_type, name)
    await message.answer("🗑️ حذف شد.")

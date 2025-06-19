from aiogram import Router, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database.db import get_all_servers, delete_server, update_server

router = Router()

class EditServerState(StatesGroup):
    choosing_field = State()
    entering_value = State()

@router.message(F.text == "🛠 مدیریت سرورها")
async def show_server_list(message: types.Message):
    servers = get_all_servers()
    if not servers:
        await message.answer("📭 هیچ سروری وجود ندارد.")
        return
    for server in servers:
        sid, protocol, country, name = server
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✏️ ویرایش", callback_data=f"edit_{sid}")],
            [InlineKeyboardButton(text="🗑 حذف", callback_data=f"del_{sid}")]
        ])
        await message.answer(f"🔹 {protocol} | {country} | {name}", reply_markup=kb)

@router.callback_query(F.data.startswith("del_"))
async def delete_selected(callback: types.CallbackQuery):
    sid = int(callback.data.split("_")[1])
    delete_server(sid)
    await callback.message.edit_text("✅ سرور حذف شد.")
    await callback.answer()

@router.callback_query(F.data.startswith("edit_"))
async def edit_selected(callback: types.CallbackQuery, state: FSMContext):
    sid = int(callback.data.split("_")[1])
    await state.update_data(server_id=sid)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="نام", callback_data="field_name")],
        [InlineKeyboardButton(text="کشور", callback_data="field_country")],
        [InlineKeyboardButton(text="کانفیگ", callback_data="field_config")]
    ])
    await callback.message.edit_text("کدوم فیلد رو می‌خوای ویرایش کنی؟", reply_markup=kb)
    await state.set_state(EditServerState.choosing_field)

@router.callback_query(F.data.startswith("field_"))
async def ask_new_value(callback: types.CallbackQuery, state: FSMContext):
    field = callback.data.split("_")[1]
    await state.update_data(field=field)
    await callback.message.edit_text(f"مقدار جدید برای {field} رو بفرست:")
    await state.set_state(EditServerState.entering_value)

@router.message(EditServerState.entering_value)
async def apply_edit(message: types.Message, state: FSMContext):
    data = await state.get_data()
    server_id = data["server_id"]
    field = data["field"]
    value = message.text

    update_server(server_id, field, value)
    await message.answer("✅ ویرایش انجام شد.")
    await state.clear()

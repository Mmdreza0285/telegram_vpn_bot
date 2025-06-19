from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database.db import get_user_info, get_all_user_ids

router = Router()

class BroadcastState(StatesGroup):
    waiting_for_message = State()

@router.message(F.text == "📬 پیام همگانی")
async def ask_for_broadcast(message: Message, state: FSMContext):
    info = get_user_info(message.from_user.id)
    if not info or info["role"] != "admin":
        await message.answer("⛔ فقط ادمین به این بخش دسترسی داره.")
        return
    await message.answer("📝 لطفاً پیام همگانی رو ارسال کن (متن یا مدیا)")
    await state.set_state(BroadcastState.waiting_for_message)

@router.message(BroadcastState.waiting_for_message)
async def broadcast_message(message: Message, state: FSMContext, bot):
    user_ids = get_all_user_ids()
    success = 0
    fail = 0
    for uid in user_ids:
        try:
            await message.send_copy(uid)
            success += 1
        except:
            fail += 1

    await message.answer(f"📬 پیام برای {success} کاربر با موفقیت ارسال شد ✅\n❌ ناموفق: {fail}")
    await state.clear()

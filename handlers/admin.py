from aiogram import Router, types, F
import os

router = Router()

@router.message(F.text == "آمار" )
async def stats(msg: types.Message):
    if msg.from_user.id != int(os.getenv("ADMIN_ID")):
        return
    await msg.answer("🔢 آمار کاربران: به زودی فعال میشه")

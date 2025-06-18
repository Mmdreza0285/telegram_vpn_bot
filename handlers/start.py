from aiogram import Router, types
from database.db import add_user
router = Router()

@router.message(commands=["start"])
async def start_handler(msg: types.Message):
    ref = msg.text.split(" ")[1] if len(msg.text.split()) > 1 else None
    add_user(msg.from_user.id, msg.from_user.username, ref)
    await msg.answer(f"سلام {msg.from_user.full_name} عزیز 🌟\nبه ربات خوش اومدی!")

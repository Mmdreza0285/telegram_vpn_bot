from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("سلام! به ربات کانفیگ VPN خوش اومدی.")

from aiogram import Router
from aiogram.types import Message
from keyboards.user_menu import user_main_menu

router = Router()

@router.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer(
        "سلام به ربات ShadowVPN خوش اومدی! 😎\nاز منوی زیر گزینه مورد نظرت رو انتخاب کن.",
        reply_markup=user_main_menu()
    )

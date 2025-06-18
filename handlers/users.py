from aiogram import Router, types

router = Router()

@router.message()
async def user_message(msg: types.Message):
    await msg.answer("از منوی اصلی گزینه‌هات رو انتخاب کن 💬")

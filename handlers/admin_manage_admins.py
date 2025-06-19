from aiogram import Router, F
from aiogram.types import Message
from database.db import get_user_info, add_admin, remove_admin, get_admins

router = Router()

@router.message(F.text == "🧑‍💼 مدیریت ادمین‌ها")
async def manage_admins(message: Message):
    info = get_user_info(message.from_user.id)
    if not info or info["role"] != "admin":
        await message.answer("⛔ فقط ادمین‌ها به این بخش دسترسی دارن.")
        return

    admins = get_admins()
    text = "🧑‍💼 ادمین‌های فعلی:\n" + "\n".join([f"`{admin_id}`" for admin_id in admins])
    text += "\n\n📌 برای افزودن ادمین، آی‌دی عددی رو بفرست یا پیامش رو فوروارد کن.\nبرای حذف، بنویس: `remove 123456789`"
    await message.answer(text, parse_mode="Markdown")

@router.message()
async def handle_admin_add_remove(message: Message):
    user_id = message.from_user.id
    info = get_user_info(user_id)
    if not info or info["role"] != "admin":
        return
    
    text = message.text.strip()
    
    # حذف
    if text.startswith("remove "):
        try:
            target_id = int(text.split(" ")[1])
            remove_admin(target_id)
            await message.answer(f"✅ ادمین با ID `{target_id}` حذف شد.", parse_mode="Markdown")
        except:
            await message.answer("❌ فرمت اشتباهه. مثال: `remove 123456789`", parse_mode="Markdown")
        return

    # افزودن با فوروارد
    if message.forward_from:
        add_admin(message.forward_from.id)
        await message.answer(f"✅ ادمین با آی‌دی `{message.forward_from.id}` افزوده شد.", parse_mode="Markdown")
        return

    # افزودن با آی‌دی مستقیم
    try:
        target_id = int(text)
        add_admin(target_id)
        await message.answer(f"✅ ادمین با ID `{target_id}` افزوده شد.", parse_mode="Markdown")
    except:
        pass  # نادیده بگیر

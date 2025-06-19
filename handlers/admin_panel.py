from database.db import get_user_info

@dp.message(F.text == "🛠️ پنل مدیریت")
async def admin_panel(message: Message):
    user_id = message.from_user.id
    user_info = get_user_info(user_id)
    
    if not user_info or user_info["role"] != "admin":
        await message.answer("🚫 فقط ادمین‌ها به این بخش دسترسی دارن.")
        return
    
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton("📊 آمار ربات"), KeyboardButton("📬 پیام همگانی")],
        [KeyboardButton("🧑‍💼 مدیریت ادمین‌ها"), KeyboardButton("🔗 تنظیم کانال عضویت")],
        [KeyboardButton("📥 مدیریت سرورها")],
        [KeyboardButton("🎨 تنظیم پیام‌ها"), KeyboardButton("📲 مدیریت کلاینت‌ها")],
        [KeyboardButton("⏱️ زمان‌بندی ارسال سرورها")],
        [KeyboardButton("🔙 بازگشت")]
    ])
    
    await message.answer("🛠️ پنل مدیریت فعال شد:", reply_markup=kb)

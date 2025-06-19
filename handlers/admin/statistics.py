@router.message(F.text == "📈 آمار رفرال‌ها")
async def all_ref_stats(message: Message):
    if message.from_user.id not in ADMINS:
        return
    result = cursor.execute("SELECT ref_id, COUNT(*) as total FROM users WHERE ref_id IS NOT NULL GROUP BY ref_id ORDER BY total DESC").fetchall()
    text = "📊 آمار رفرال:\n\n"
    for row in result:
        ref, count = row
        text += f"👤 {ref} ➜ {count} نفر\n"
    await message.answer(text or "هیچ رفرالی ثبت نشده.")

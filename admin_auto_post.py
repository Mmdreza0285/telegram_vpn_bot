from aiogram import Router, F
from aiogram.types import Message
from database.db import get_all_auto_servers
from config import CHANNEL_ID, ADMINS
import asyncio

router = Router()

@router.message(F.text == "📥 ارسال خودکار به کانال", F.from_user.id.in_(ADMINS))
async def post_servers(msg: Message):
    servers = await get_all_auto_servers()
    if not servers:
        await msg.answer("هیچ سروری برای ارسال وجود ندارد.")
        return

    for srv in servers:
        await msg.bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"{srv['name']}\n{srv['config']}"
        )
        await asyncio.sleep(2)

    await msg.answer("✅ سرورها به کانال ارسال شدند.")

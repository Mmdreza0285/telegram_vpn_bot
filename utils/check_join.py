from database.db import get_channels
from aiogram.types import User
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

async def check_user_joined(user: User, bot: Bot):
    channels = get_channels()
    not_joined = []

    for channel in channels:
        try:
            member = await bot.get_chat_member(f"@{channel}", user.id)
            if member.status in ['left', 'kicked']:
                not_joined.append(channel)
        except TelegramBadRequest:
            not_joined.append(channel)

    return not_joined

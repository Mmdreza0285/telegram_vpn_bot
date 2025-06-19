from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging
from start import on_start
from handlers.admin_panel import register_admin_handlers
from handlers.user_menu import register_user_handlers
from database import db

API_TOKEN = 'توکن_ربات_اینجا'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

register_admin_handlers(dp)
register_user_handlers(dp)

@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    await on_start(message, bot)

if __name__ == '__main__':
    from database import db  # ساخت دیتابیس در شروع
    executor.start_polling(dp, skip_updates=True)

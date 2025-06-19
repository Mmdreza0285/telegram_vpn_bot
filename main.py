import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils import executor
from database.db import init_db
from handlers import start, admin_add_server, admin_edit_server, admin_manage_admins, admin_channels, user_get_servers, account, referral

logging.basicConfig(level=logging.INFO)

async def on_startup(bot: Bot):
    init_db()

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    # ثبت هندلرها
    dp.include_router(start.router)
    dp.include_router(admin_add_server.router)
    dp.include_router(admin_edit_server.router)
    dp.include_router(admin_manage_admins.router)
    dp.include_router(admin_channels.router)
    dp.include_router(user_get_servers.router)
    dp.include_router(account.router)
    dp.include_router(referral.router)

    # اجرای ربات
    await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(main(), skip_updates=True)

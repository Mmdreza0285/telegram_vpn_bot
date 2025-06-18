# main.py

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

from config import BOT_TOKEN, ADMINS
from handlers.user import start, donate, referral, download_clients, free_servers, contact_admin, account_status
from handlers.admin import panel, add_server, edit_server, broadcast, stats, manage_admins, manage_clients

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    # ثبت هندلرهای کاربران
    start.register(dp)
    donate.register(dp)
    referral.register(dp)
    download_clients.register(dp)
    free_servers.register(dp)
    contact_admin.register(dp)
    account_status.register(dp)

    # ثبت هندلرهای ادمین
    panel.register(dp)
    add_server.register(dp)
    edit_server.register(dp)
    broadcast.register(dp)
    stats.register(dp)
    manage_admins.register(dp)
    manage_clients.register(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from handlers import start, admin, users
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# ثبت هندلرها
start.register_handlers(dp)
admin.register_handlers(dp)
users.register_handlers(dp)

async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="شروع ربات")
    ])
    print("ربات روشن شد")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

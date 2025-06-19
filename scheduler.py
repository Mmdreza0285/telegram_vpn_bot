from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.db import get_next_server, mark_server_sent, get_auto_name
import asyncio
import config

scheduler = AsyncIOScheduler()

async def send_scheduled_server(bot: Bot):
    data = get_next_server()
    if not data:
        return
    server_id, server_text = data
    label = get_auto_name() or "shadoowvpnn"
    formatted = f"{label}\n\n{server_text}"
    try:
        await bot.send_message(chat_id=config.CHANNEL_ID, text=formatted)
        mark_server_sent(server_id)
    except Exception as e:
        print("❌ Error sending server:", e)

def start_scheduler(bot: Bot):
    scheduler.add_job(send_scheduled_server, 'interval', hours=1, args=[bot])
    scheduler.start()

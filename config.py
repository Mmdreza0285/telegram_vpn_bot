import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = [int(i) for i in os.getenv("ADMINS", "").split(",")]
CHANNEL_ID = os.getenv("CHANNEL_ID")

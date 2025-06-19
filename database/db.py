# database/db.py

import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# جدول کاربران
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    referral_by INTEGER,
    join_date TEXT
)
""")

# جدول کانفیگ‌ها (برای اهدایی)
cursor.execute("""
CREATE TABLE IF NOT EXISTS configs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    protocol TEXT,
    country TEXT,
    config_data TEXT,
    created_at TEXT
)
""")

# جدول سرورهای ادمین
cursor.execute("""
CREATE TABLE IF NOT EXISTS servers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    protocol TEXT,
    country TEXT,
    name TEXT,
    config_data TEXT,
    active INTEGER DEFAULT 1
)
""")

# جدول رفرال‌ها
cursor.execute("""
CREATE TABLE IF NOT EXISTS referrals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    referrer_id INTEGER,
    referred_id INTEGER,
    date TEXT
)
""")

conn.commit()


# ---------------------------- 📌 توابع ----------------------------

def create_user_if_not_exists(user_id: int, username="", full_name="", referral_by=None):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    if not cursor.fetchone():
        from datetime import datetime
        cursor.execute("""
            INSERT INTO users (user_id, username, full_name, referral_by, join_date)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, username, full_name, referral_by, datetime.now().strftime("%Y-%m-%d %H:%M")))
        conn.commit()

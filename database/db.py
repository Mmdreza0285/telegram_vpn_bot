import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# جدول‌ها و توابع
def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        ref_id INTEGER
    )""")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        protocol TEXT,
        country TEXT,
        name TEXT,
        config TEXT,
        added_by INTEGER
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS required_channels (
        channel_username TEXT PRIMARY KEY
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_configs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        config TEXT,
        protocol TEXT,
        country TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS referrals (
        user_id INTEGER PRIMARY KEY,
        referrer_id INTEGER
    )""")
    
    conn.commit()

# سایر توابع مورد نیاز مانند `add_server`, `get_all_servers`, `add_required_channel`

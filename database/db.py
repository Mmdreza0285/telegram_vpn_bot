import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

# جدول‌های مورد نیاز
def init_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        ref_id INTEGER
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS servers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        protocol TEXT,
        country TEXT,
        name TEXT,
        config TEXT,
        added_by INTEGER
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS required_channels (
        channel_username TEXT PRIMARY KEY
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_configs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        config TEXT,
        protocol TEXT,
        country TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS referrals (
        user_id INTEGER PRIMARY KEY,
        referrer_id INTEGER
    )''')

    conn.commit()

# سایر توابع مورد نیاز
def add_server(protocol, country, name, config, added_by):
    cursor.execute("INSERT INTO servers (protocol, country, name, config, added_by) VALUES (?, ?, ?, ?, ?)",
                   (protocol, country, name, config, added_by))
    conn.commit()

def get_all_servers():
    cursor.execute("SELECT id, protocol, country, name FROM servers")
    return cursor.fetchall()

def add_required_channel(channel_username):
    cursor.execute("INSERT INTO required_channels (channel_username) VALUES (?)", (channel_username,))
    conn.commit()

def delete_required_channel(channel_username):
    cursor.execute("DELETE FROM required_channels WHERE channel_username = ?", (channel_username,))
    conn.commit()

def get_required_channels():
    cursor.execute("SELECT channel_username FROM required_channels")
    return [row[0] for row in cursor.fetchall()]

# سایر توابع دیتابیس مورد نیاز مشابه

import sqlite3

def create_db():
    conn = sqlite3.connect("bot.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        referrer INTEGER,
        downloads INTEGER DEFAULT 0
    )""")
    conn.commit()
    conn.close()

def add_user(user_id, username, referrer=None):
    conn = sqlite3.connect("bot.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (id, username, referrer) VALUES (?, ?, ?)",
              (user_id, username, referrer))
    conn.commit()
    conn.close()

import sqlite3

# اتصال به دیتابیس
conn = sqlite3.connect("bot_data.db")
cursor = conn.cursor()

# ایجاد جدول کاربران
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    ref_by INTEGER DEFAULT 0,
    joined_at TEXT
)
""")

# ایجاد جدول سرورها
cursor.execute("""
CREATE TABLE IF NOT EXISTS servers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    config TEXT,
    protocol TEXT,
    country TEXT,
    auto_post INTEGER DEFAULT 0
)
""")

# ایجاد جدول کلاینت‌ها (در صورت نیاز)
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    url TEXT
)
""")

# ذخیره کاربر جدید
def save_user(user_id, username, first_name, ref_by, joined_at):
    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, username, first_name, ref_by, joined_at)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, username, first_name, ref_by, joined_at))
    conn.commit()

# دریافت همه کاربران
def get_all_users():
    cursor.execute("SELECT user_id FROM users")
    return cursor.fetchall()

# دریافت همه سرورهای auto_post
def get_all_auto_servers():
    cursor.execute("SELECT name, config FROM servers WHERE auto_post = 1")
    return cursor.fetchall()

# تغییر نام همه سرورها
def update_all_server_names(new_name):
    cursor.execute("UPDATE servers SET name = ?", (new_name,))
    conn.commit()

# اضافه کردن سرور جدید
def add_server(name, config, protocol, country, auto_post=0):
    cursor.execute("""
        INSERT INTO servers (name, config, protocol, country, auto_post)
        VALUES (?, ?, ?, ?, ?)
    """, (name, config, protocol, country, auto_post))
    conn.commit()

# دریافت تعداد کاربران
def get_user_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

import sqlite3
from datetime import datetime

# اتصال به دیتابیس
conn = sqlite3.connect("bot_data.db")
cursor = conn.cursor()

# ✅ ایجاد جدول کاربران
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    ref_by INTEGER DEFAULT 0,
    joined_at TEXT
)
""")

# ✅ جدول سرورها
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

# ✅ جدول کلاینت‌ها
cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    url TEXT
)
""")

# ✅ جدول رفرال‌ها (اختیاری، اگر نیاز به جزئیات بیشتر باشه)
cursor.execute("""
CREATE TABLE IF NOT EXISTS referrals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    referred_user_id INTEGER,
    created_at TEXT
)
""")

conn.commit()

# ✅ ذخیره کاربر جدید
def save_user(user_id, username, first_name, ref_by):
    joined_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT OR IGNORE INTO users (user_id, username, first_name, ref_by, joined_at)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, username, first_name, ref_by, joined_at))
    conn.commit()
    if ref_by != 0:
        cursor.execute("""
            INSERT INTO referrals (user_id, referred_user_id, created_at)
            VALUES (?, ?, ?)
        """, (ref_by, user_id, joined_at))
        conn.commit()

# ✅ تعداد کاربران
def get_user_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

# ✅ گرفتن لیست تمام یوزرها
def get_all_users():
    cursor.execute("SELECT user_id FROM users")
    return [user[0] for user in cursor.fetchall()]

# ✅ گرفتن تعداد رفرال‌های هر کاربر
def get_referral_count(user_id):
    cursor.execute("SELECT COUNT(*) FROM referrals WHERE user_id = ?", (user_id,))
    return cursor.fetchone()[0]

# ✅ افزودن سرور
def add_server(name, config, protocol, country, auto_post=0):
    cursor.execute("""
        INSERT INTO servers (name, config, protocol, country, auto_post)
        VALUES (?, ?, ?, ?, ?)
    """, (name, config, protocol, country, auto_post))
    conn.commit()

# ✅ گرفتن همه سرورها
def get_all_servers():
    cursor.execute("SELECT * FROM servers")
    return cursor.fetchall()

# ✅ گرفتن سرورها بر اساس پروتکل
def get_servers_by_protocol(protocol):
    cursor.execute("SELECT * FROM servers WHERE protocol = ?", (protocol,))
    return cursor.fetchall()

# ✅ گرفتن سرورها بر اساس کشور
def get_servers_by_country(country):
    cursor.execute("SELECT * FROM servers WHERE country = ?", (country,))
    return cursor.fetchall()

# ✅ گرفتن سرورهای auto_post
def get_auto_post_servers():
    cursor.execute("SELECT name, config FROM servers WHERE auto_post = 1")
    return cursor.fetchall()

# ✅ ویرایش نام همه سرورها
def update_all_server_names(new_name):
    cursor.execute("UPDATE servers SET name = ?", (new_name,))
    conn.commit()

# ✅ اضافه‌کردن کلاینت
def add_client(name, url):
    cursor.execute("INSERT INTO clients (name, url) VALUES (?, ?)", (name, url))
    conn.commit()

# ✅ گرفتن همه کلاینت‌ها
def get_all_clients():
    cursor.execute("SELECT * FROM clients")
    return cursor.fetchall()

# ✅ حذف یک کلاینت
def delete_client(client_id):
    cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    conn.commit()

# ✅ حذف یک سرور
def delete_server(server_id):
    cursor.execute("DELETE FROM servers WHERE id = ?", (server_id,))
    conn.commit()

# ✅ گرفتن کاربر بر اساس ID
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    return cursor.fetchone()

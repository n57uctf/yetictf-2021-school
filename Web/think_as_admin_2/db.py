import sqlite3


DATABASE = 'static/data.db'


def init_db():
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            login TEXT,
            password TEXT,
            info TEXT);
        """)
        conn.commit()
    except Exception as e:
        return e
    return True


def login(username, password):
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("""
            SELECT info FROM users WHERE login='""" + username + """' and password='""" + password + """';
        """)
        data = cur.fetchall()
        conn.close()
        return data
    except:
        return None

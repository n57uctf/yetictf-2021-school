import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()


"""структура:
email - уникальный email
loign - уникальный логин
password - hash sha256 от пароля
uuid - уникальный идентификатор
card_number - номер карты (виза) уникальный
balance_card - по умолчанию 0
balance - стандартный баланс, по умолчанию 0
"""

c.execute("""CREATE TABLE IF NOT EXISTS 
users(id INTEGER PRIMARY KEY, login TEXT, email TEXT, password TEXT, balance INT, uuid TEXT, card_number TEXT, balance_card INT)""")
conn.commit()
conn.close()
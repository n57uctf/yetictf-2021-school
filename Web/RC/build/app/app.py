from flask import Flask, render_template, request, g, redirect, make_response, session
import sqlite3
from time import sleep
from uuid import uuid4
from hashlib import sha256
from re import compile

app = Flask(__name__)
app.database = "database.db"
app.secret_key = "QSKMALKMKMASDOASFASFIWDJ898*&SD*A&H"
email_pattern = compile('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
visa_pattern = compile("4\d{15}")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def connect_db():
    return sqlite3.connect(app.database)

@app.route('/', methods=['GET'])
def index_raw():
    if not session:
        return make_response(redirect('/login'))
    else:
        return make_response(redirect('/index#info'))

@app.route('/exit', methods=['GET', 'POST'])
def exit():
    session.clear()
    return make_response(redirect('/'))

@app.route('/index', methods=["GET"])
def index():
    try:
        uuid = session['token']
    except:
        return make_response(redirect('/login'))
    g.db = connect_db()
    user = g.db.execute("SELECT login FROM users WHERE uuid=?", (uuid)).fetchone()[0]
    balance = g.db.execute("SELECT balance FROM users WHERE uuid=?", (uuid)).fetchone()[0]
    balance_card = g.db.execute("SELECT balance_card FROM users WHERE uuid=?", (uuid)).fetchone()[0]
    secret = "yetiCTF{fastest_request_on_wild_fintech}" if balance_card >= 700 else ""
    if user:
            return render_template("index.html", balance=balance, balance_card=balance_card, secret=secret)
    else:
        return make_response(redirect('/login'))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        g.db = connect_db()
        email = request.form.get('email')
        login = request.form.get('login')
        password = sha256(request.form.get("password").encode()).hexdigest()
        card_number = request.form.get('card').replace(' ', '')
        uuid = str(uuid4())
        unique_login = g.db.execute("SELECT COUNT(login) FROM users WHERE login=?", (login,)).fetchone()[0]
        if unique_login != 0:
            g.db.close()
            return render_template('register.html', error="Такой пользователь уже существует в системе")
        unique_email = g.db.execute("SELECT COUNT(email) FROM users WHERE email=?", (email,)).fetchone()[0]
        if unique_email != 0:
            g.db.close()
            return render_template('register.html', error="Такой емейл уже существует в системе")
        unique_card = g.db.execute("SELECT COUNT(card_number) FROM users WHERE card_number=?", (card_number,)).fetchone()[0]
        if unique_card != 0:
            g.db.close()
            return render_template('register.html', error='Такая карта уже добавлена в систему')
        if not email_pattern.match(email):
            return render_template('register.html', error='Неверный формат email-адреса')
        if not visa_pattern.match(card_number):
            return render_template('register.html', error='Неверный формат карты Visa')
        g.db.execute("""INSERT INTO users(login,password,email,uuid,balance,card_number,balance_card) 
        VALUES (?,?,?,?,?,?,?)""", (login,password,email,uuid,50,card_number,0))
        g.db.commit()
        g.db.close()
        return (make_response(redirect('/login')))
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form.get('login')
        password = sha256(request.form.get("password").encode()).hexdigest()
        g.db = connect_db()
        uuid = g.db.execute("""SELECT uuid FROM users WHERE 
        (login = ? or email = ?) AND password = ?""", (login, login, password)).fetchone()
        if uuid:
            session['token'] = uuid 
            return make_response(redirect('/index#info'))
        else:
            return render_template('login.html', error="Ошибка. Попробуйте еще раз.")
    return render_template('login.html')


@app.route("/transaction", methods=["GET", "POST"])
def transaction():
    try:
        uuid = session['token']
    except:
        return make_response(redirect('/login'))
    if request.method == "POST":
        g.db = connect_db()
        count = request.form.get('count')
        try:
            count = int(count)
        except:
            return render_template("transaction.html", response='Укажите целое число для перевода.')
        balance = g.db.execute("SELECT balance FROM users WHERE uuid = ?", (uuid[0],)).fetchone()[0]
        if count <= 0:
            return render_template("transaction.html", response="Невозможен перевод средств меньше или равных 0.")
        if balance >= count:
            sleep(1)
            g.db.execute("UPDATE users SET balance=balance-? WHERE uuid=?", (count, uuid[0]))
            g.db.execute("UPDATE users SET balance_card=balance_card+? WHERE uuid=?", (count, uuid[0]))
            g.db.commit()
            g.db.close()
            return render_template("transaction.html", response="Перевод с баланса на карту успешно выполнен!")
        else:
            return render_template("transaction.html", response="На Вашем балансе недостаточно средств для перевода.")
    return render_template("transaction.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, threaded=True)
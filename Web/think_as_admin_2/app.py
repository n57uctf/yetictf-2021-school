from flask import Flask, request, render_template
import db

app = Flask(__name__)
db.init_db()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        data = db.login(username, password)
        if not data:
            return render_template('login.html', result='Wrong password')
        else:
            strdata = ''
            for i in data:
                for j in i:
                    strdata += j + '\n'
                strdata += '\n'
            return strdata


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=False)

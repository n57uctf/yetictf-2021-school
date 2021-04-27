from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    agent = request.headers.get('User-Agent')
    if agent == 'admin':
        return 'Hello admin flag is yetiCTF{g00d_j0b_agent_1s_adm1n}'
    else:
        return 'You are not a admin'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=False)

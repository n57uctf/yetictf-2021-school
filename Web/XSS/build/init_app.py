from flask import Flask
from logic import index, report, download, admin
from jobs import rq

def create_app():
    app = Flask(__name__)
    app.config['CURRENT_URL'] =  '127.0.0.1:8080'

    rq.init_app(app)

    app.add_url_rule('/', 'index', index, methods=["GET", "POST"])
    app.add_url_rule('/report', 'report', report, methods=["GET", "POST"])
    app.add_url_rule('/files/<path:filename>', '/files/<path:filename>', download)
    app.add_url_rule('/admin', 'admin', admin , methods=["GET"])
    return app
from flask import Flask

app = Flask(__name__)


@app.route('/app')
def index():
    return "IT IS FLASK APP 1 -RSRC"


if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    app.debug = True
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
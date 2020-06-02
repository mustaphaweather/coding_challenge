from . import create_app
from gevent.pywsgi import WSGIServer

application = create_app()
server = WSGIServer(('127.0.0.1', 5000), application)
server.serve_forever()
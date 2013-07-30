from gevent.wsgi import WSGIServer
from floober import app

http_server = WSGIServer(('', 5000),app)
http_server.serve_forever()


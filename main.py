from werkzeug.middleware.dispatcher import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication

import soap_service
from flask_server import app


app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/soap': WsgiApplication(soap_service.create_app(app))
})

if __name__ == '__main__':
    app.run(ssl_context='adhoc')

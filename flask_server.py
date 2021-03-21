import json
from flask import Flask, make_response, current_app

app = Flask(__name__)
app.config.from_object('config.LocalConfig')

@app.route('/hello')
def hello():
    response = make_response(json.dumps({
        'hello': current_app.config['HELLO'],
    }))
    response.headers['Content-Type'] = 'application/json'
    return response

from flask import Flask
from flask import Response
flask_app = Flask('flaskapp')


@flask_app.route('/hello')
def hello_world():
    return Response(
        'Hello world from Flask! This is Shahron buddy!\n',
        mimetype='text/plain'
    )

app = flask_app.wsgi_app

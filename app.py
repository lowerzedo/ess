from flask import Flask, request
from config import *
from routes.blueprint import blueprint

@blueprint.after_request
def set_cors(response):
    origin = request.headers.get('Origin')
    response.headers['Access-Control-Allow-Origin'] = origin
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT'
    response.headers['Content-Type'] = 'application/json'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/ess-temp')

if APP_ENV != 'production':
    app.debug = True


if __name__ == '__main__':  # Running the app
    app.run()
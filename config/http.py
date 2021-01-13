from flask import Flask
from flask_cors import CORS
from flask_compress import Compress
from flask_swagger_ui import get_swaggerui_blueprint

from helpers import jwtmanager
from helpers import postgre_alchemy
import routes

cors = CORS()
compress = Compress()


def createApp(configuration):
    app = Flask(
        __name__.split(',')[0],
        static_url_path='/static',
        static_folder='../static')

    # swagger specific server
    SWAGGER_URL = '/boilerplate-flask'
    API_URL = '/boilerplate-flask/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Boilerplate API",
            'base_url': ''
        }
    )

    # register route blueprint
    app.register_blueprint(routes.index.bp)
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix="/documentation")
    app.register_blueprint(routes.error.bp)

    # load configuration
    app.config.from_object(configuration)

    # init app
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    compress.init_app(app)
    jwtmanager.init_app(app)
    postgre_alchemy.init_app(app)

    return app

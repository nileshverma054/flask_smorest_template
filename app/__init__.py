import os

from flask import Flask

from app.blueprint import register_routing
from app.extension import api
from app.utils.core_utils import after_request, before_request, handle_uknown_exceptions
from app.utils.logging import config_logger


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

    # initialize external dependencies
    api.init_app(app)

    # configure logging
    config_logger(app)

    # Register Blueprint
    register_routing(api)

    # Register error handlers
    app.register_error_handler(Exception, handle_uknown_exceptions)
    app.register_error_handler(500, handle_uknown_exceptions)

    # Register flask functions
    app.before_request(before_request)
    app.after_request(after_request)

    return app


settings_module = os.getenv("APP_SETTINGS_MODULE")
app = create_app(settings_module)

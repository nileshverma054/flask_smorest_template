import os


class DefaultConfig:
    """
    Default Configuration
    """

    # Flask Configuration
    APP_NAME = os.environ.get("APP_NAME")
    PROPAGATE_EXCEPTIONS = True
    DEBUG = False
    TESTING = False

    # Config API documents
    API_TITLE = "Flask-smorest API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    # Swagger UI Config
    OPENAPI_SWAGGER_UI_PATH = "/doc/"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # ReDoc Confi
    OPENAPI_REDOC_PATH = "/redoc/"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    # Rapiddoc
    OPENAPI_RAPIDOC_PATH = "/rapidoc/"
    OPENAPI_RAPIDOC_URL = "https://unpkg.com/rapidoc/dist/rapidoc-min.js"

    # App Environments
    APP_ENV_LOCAL = "local"
    APP_ENV_TESTING = "testing"
    APP_ENV_DEVELOP = "dev"
    APP_ENV_PRODUCTION = "production"

    # Logging
    DATE_FMT = "%Y-%m-%d %H:%M:%S"


class LocalConfig(DefaultConfig):
    # App environment
    APP_ENV = DefaultConfig.APP_ENV_LOCAL

    # Activate debug mode
    DEBUG = True


class TestingConfig(DefaultConfig):
    # App environment
    APP_ENV = DefaultConfig.APP_ENV_TESTING

    # Flask disables error catching during request handling for better error reporting in tests
    TESTING = True

    # Activate debug mode
    DEBUG = True


class DevelopConfig(DefaultConfig):
    # App environment
    APP_ENV = DefaultConfig.APP_ENV_DEVELOP

    # Activate debug mode
    DEBUG = False


class ProductionConfig(DefaultConfig):
    # App environment
    APP_ENV = DefaultConfig.APP_ENV_PRODUCTION

    # Activate debug mode
    DEBUG = False

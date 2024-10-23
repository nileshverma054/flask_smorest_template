import logging
import logging.config
import uuid

import flask

from app.config import DefaultConfig

request_id = str(uuid.uuid4())
log_format = (
    "%(request_id)s - "
    "%(asctime)s - "
    "%(levelname)8s - "
    "%(filename)s:%(lineno)s - "
    "%(message)s"
)


def get_request_id():
    """
    Retrieves the request ID for the current Flask request.

    Returns:
        str: The request ID.

    Raises:
        None.
    """
    if flask.has_request_context():
        if getattr(flask.g, "request_id", None):
            return getattr(flask.g, "request_id", "")
        headers = flask.request.headers
        # if we are using AWS ELB then the "X-Amzn-Trace-Id" is already set which
        # can be used to trace the API request lifecycle
        flask.g.request_id = headers.get("X-Amzn-Trace-Id") or str(uuid.uuid4())
        return flask.g.request_id
    return request_id


class RequestIdFilter(logging.Filter):
    """
    A logging filter which adds a request ID to each log record.

    This filter is used to add a request ID to each log record. The request ID
    is taken from the current Flask request context, if available. If not
    available, a new request ID is generated.

    Attributes:
        None.
    """

    def filter(self, record):
        record.request_id = get_request_id()
        return True


class CustomFormatter(logging.Formatter):
    grey = "\x1b[37;20m"
    white = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey + log_format + reset,
        logging.INFO: white + log_format + reset,
        logging.WARNING: yellow + log_format + reset,
        logging.ERROR: red + log_format + reset,
        logging.CRITICAL: bold_red + log_format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def config_logger(app):
    """
    Configures the application logger.

    This function configures the application logger with a filter
    to add a request ID to each log record.

    Args:
        app (Flask): The Flask application..

    Returns:
        None.

    Raises:
        None.
    """
    log_config = dict(
        version=1,
        disable_existing_loggers=True,
        filters={
            "request_id": {"()": RequestIdFilter},
        },
        formatters={
            "console": {
                "()": CustomFormatter,
            }
        },
        handlers={
            "console": {
                "level": app.config.get("LOG_LEVEL", "DEBUG"),
                "class": "logging.StreamHandler",
                "formatter": "console",
                "filters": ["request_id"],
            }
        },
        loggers={
            "root": {
                "handlers": ["console"],
                "level": app.config.get("LOG_LEVEL", "DEBUG"),
                "propagate": False,
            }
        },
    )

    # disable flask development server logs
    if app.config.get("APP_ENV") != DefaultConfig.APP_ENV_LOCAL:
        log = logging.getLogger("werkzeug")
        log.setLevel(logging.WARNING)

    logging.config.dictConfig(log_config)

    app.logger = logging.getLogger("console")

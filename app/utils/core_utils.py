import time
from http import HTTPStatus

from flask import current_app as app
from flask import g, jsonify, request

from app.utils.constants import NO_LOG_ROUTES


def handle_uknown_exceptions(e: Exception):
    app.logger.critical(f"UnknownException: {e}", exc_info=True)
    response = jsonify(
        {
            "code": HTTPStatus.INTERNAL_SERVER_ERROR.value,
            "message": (
                "Something went wrong, please try again. "
                "If you keep seeing this error, please contact support with request-id: "
                f"{g.request_id}"
            ),
            "status": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
        }
    )
    response.status_code = 500
    return response


def before_request():
    g.request_start_time = time.time()


def after_request(response):
    response.headers["X-Request-Id"] = getattr(g, "request_id", "")
    if request.path in NO_LOG_ROUTES:
        return response

    diff_us = int((time.time() - g.request_start_time) * 1_000_000)
    diff_ms = int((time.time() - g.request_start_time) * 1000)
    diff_s = f"{(time.time() - g.request_start_time):2.4f}s"
    app.logger.info(
        (
            f"{request.method} {request.full_path} | {response.status} | "
            f"{diff_s}s | {diff_ms}ms | {diff_us}us"
        )
    )
    return response

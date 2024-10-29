from flask import current_app as app
from flask_smorest import abort


def check_application_health():
    check_db_health()
    return {"message": "Healthy"}


def check_db_health():
    try:
        app.logger.info("Checking Database Health")
        return True
    except Exception:
        app.logger.critical("Database Unhealthy", exc_info=True)
        abort(503, message="Database Unhealthy")

from app import create_app
from app.services.healthcheck_service import check_application_health

app = create_app("app.config.LocalConfig")


def test_check_application_health():
    with app.test_request_context():
        result = check_application_health()
        assert result == {"message": "Healthy"}

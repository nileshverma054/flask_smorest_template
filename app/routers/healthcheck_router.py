from flask.views import MethodView
from flask_smorest import Blueprint
from app.schemas.healthcheck_schema import HealthcheckResponseSchema

blp = Blueprint("Healthcheck", __name__, description="API Healthcheck")


@blp.route("/")
class Healthcheck(MethodView):
    @blp.response(200, HealthcheckResponseSchema)
    @blp.response(200)
    @blp.doc(security=[])
    def get(self):
        """
        Healthcheck API endpoint.

        Returns:
            dict: A dictionary with the status of the App.
        """
        return {"message": "Healthy"}

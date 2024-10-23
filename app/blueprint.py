from flask_smorest import Api

from app.routers.healthcheck_router import blp as HealthcheckBlueprint


# Register Blueprint
def register_routing(api: Api):
    api.register_blueprint(HealthcheckBlueprint)

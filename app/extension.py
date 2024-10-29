from flask_smorest import Api

# Adding Auth to Doc - https://github.com/marshmallow-code/flask-smorest/issues/36
api = Api(
    spec_kwargs={
        "title": "Flask-smorest API",
        "host": "localhost",
        "version": "1.0.0",
        "x-internal-id": "1"
    }
)

from marshmallow import Schema, fields


class HealthcheckResponseSchema(Schema):
    message = fields.String()

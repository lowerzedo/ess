from marshmallow import Schema, fields, validate

not_empty = validate.Length(min=1, error='Field cannot be empty')


class UpdateDateSchema(Schema):
    column = fields.String(required=True, validate=not_empty)
    nno = fields.String(required=True, validate=not_empty)
    date = fields.String(required=False)




from flask_restful import fields

lang_fields = {
    'name': fields.String,
    'amount': fields.Float
}

stats_fields = {
    'langs': fields.List(fields.Nested(lang_fields))
}

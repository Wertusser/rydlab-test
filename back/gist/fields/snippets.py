from flask_restful import fields

file_fields = {
    'filename': fields.String,
    'text': fields.String,
    'extension': fields.String,
    'is_binary': fields.Boolean
}

snippet_fields = {
    "snippet_id": fields.String,
    "title": fields.String,
    "description": fields.String,
    "created_at": fields.DateTime,
    "is_public": fields.Boolean,
    "files": fields.List(fields.Nested(file_fields))
}

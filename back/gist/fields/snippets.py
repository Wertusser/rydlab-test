from flask_restful import fields
from collections import Counter


class Statistic(fields.Raw):
    def format(self, value):
        ext = [file.extension for file in value]
        return Counter(ext).most_common()


def format_file(snippet):
    file = snippet.files[0]
    lines = file.text.split("\n")
    file.text = "\n".join(lines[:10]) + "\n..." * (len(lines) > 10)
    return file


file_fields = {
    'filename': fields.String,
    'text': fields.String,
    'extension': fields.String
}

snippet_fields = {
    "snippet_id": fields.String,
    "title": fields.String,
    "created_at": fields.DateTime,
    "is_public": fields.Boolean,
    "files": fields.List(fields.Nested(file_fields)),
    "isFull": fields.Boolean(default=True)
}

snippet_list_fields = {
    "snippet_id": fields.String,
    "title": fields.String,
    "created_at": fields.DateTime,
    "is_public": fields.Boolean,
    "file": fields.Nested(file_fields, attribute=format_file),
    "statistic": Statistic(attribute="files"),
    "isFull": fields.Boolean(default=False)
}

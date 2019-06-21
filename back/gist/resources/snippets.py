from flask import request
from flask_restful import Resource, abort
from gist.models import Snippet, File
from datetime import datetime


class ApiSnippet(Resource):
    def get(self, snippet_id):
        snippet = Snippet.get_or_none(Snippet.snippet_id == snippet_id)
        if snippet:
            return snippet, 200
        else:
            abort(404, message="Snippet doesn't exist!")


class ApiSnippetList(Resource):
    def get(self):
        query = Snippet.select().where(Snippet.is_public)
        snippets = [snippet for snippet in query]
        return snippets, 200

    def post(self):
        data = request.data["json"]
        snippet = Snippet.create(title=data.get("title", ""),
                                 description=data.get("description", ""),
                                 created_at=datetime.now())
        for file in data.get("files", []):
            filename = file.get("filename", "")
            File.create(snippet=snippet,
                        filename=filename,
                        extension=filename.split(".")[-1],
                        is_binary=False)
        return snippet, 200

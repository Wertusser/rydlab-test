from flask import request
from flask_restful import Resource, abort, marshal_with
from gist.models import Snippet, File
from gist.fields.snippets import snippet_fields


class ApiSnippet(Resource):
    @marshal_with(snippet_fields, envelope="result")
    def get(self, snippet_id):
        snippet = Snippet.get_or_none(Snippet.snippet_id == snippet_id)
        if snippet:
            return snippet, 200
        else:
            abort(404, message="Snippet doesn't exist!")


class ApiSnippetList(Resource):
    @marshal_with(snippet_fields, envelope="result")
    def get(self):
        query = Snippet\
            .select()\
            .where(Snippet.is_public)\
            .order_by(Snippet.created_at.desc())\
            .paginate(request.args.get("page", 0), 10)
        snippets = [snippet for snippet in query]
        return snippets, 200

    @marshal_with(snippet_fields, envelope="result")
    def post(self):
        data = request.get_json(force=True)
        snippet = Snippet.create(title=data.get("title", ""),
                                 description=data.get("description", ""),
                                 is_public=data.get("is_public", True))
        for file in data.get("files", []):
            filename = file.get("filename", "")
            File.create(snippet=snippet,
                        filename=filename,
                        text=file.get("text", ""),
                        extension=filename.split(".")[-1],
                        is_binary=False)
        return snippet, 200

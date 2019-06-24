from flask import request
from flask_restful import Resource, abort, marshal_with
from gist.models import Snippet, File
from gist.fields.snippets import snippet_fields
from gist.config import max_file_size


class ApiSnippet(Resource):
    @marshal_with(snippet_fields, envelope="result")
    def get(self, snippet_id):
        snippet = Snippet.get_or_none(Snippet.snippet_id == snippet_id)
        if snippet:
            return snippet, 200
        else:
            abort(400, message="Snippet doesn't exist!")


class ApiSnippetList(Resource):
    @marshal_with(snippet_fields, envelope="result")
    def get(self):
        query = Snippet \
            .select() \
            .where(Snippet.is_public) \
            .order_by(Snippet.created_at.desc()) \
            .paginate(int(request.args.get("page", 0)), 10)
        snippets = [snippet for snippet in query]
        return snippets, 200

    @marshal_with(snippet_fields, envelope="result")
    def post(self):
        data = request.get_json(force=True, silent=True)
        if not data:
            abort(400, message="Bad posted JSON data!")
        snippet = Snippet.create(title=str(data.get("title", "")),
                                 is_public=bool(data.get("is_public", True)))
        for file in data.get("files", [])[::-1]:
            if isinstance(file, dict):
                filename = str(file.get("filename", ""))
                File.create(snippet=snippet,
                            filename=filename,
                            text=str(file.get("text", "")[:max_file_size]),
                            extension=filename.split(".")[-1] or "txt")
        return snippet, 200

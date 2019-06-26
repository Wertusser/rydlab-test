from flask import request
from flask_restful import Resource, abort, marshal_with
from gist.models import Snippet, File, db
from gist.fields.snippets import snippet_fields, snippet_list_fields
from gist.config import max_file_size
from peewee import prefetch


class ApiSnippet(Resource):
    @marshal_with(snippet_fields, envelope="result")
    def get(self, snippet_id):
        snippet = Snippet.get_or_none(Snippet.snippet_id == snippet_id)
        if snippet:
            return snippet, 200
        else:
            abort(400, message="Snippet doesn't exist!")


class ApiSnippetList(Resource):
    @marshal_with(snippet_list_fields, envelope="result")
    def get(self):
        snippets_query = (Snippet.select()
                          .where(Snippet.is_public)
                          .order_by(Snippet.created_at.desc())
                          .paginate(int(request.args.get("page", 0)), 10))
        files_query = File.select()
        snippets = [snippet for snippet in prefetch(snippets_query, files_query)]
        return snippets, 200

    @marshal_with(snippet_list_fields, envelope="result")
    def post(self):
        data = request.get_json(force=True, silent=True)
        if data:
            with db.atomic():
                snippet = Snippet.create(title=str(data.get("title", "")),
                                         is_public=bool(data.get("is_public", True)))
            files = [{
                "snippet": snippet,
                "filename": str(file.get("filename", "")),
                "text": str(file.get("text", "")[:max_file_size]),
                "extension": str(file.get("filename", "")).split(".")[-1] or "txt"
            } for file in data.get("files", [])[::-1] if isinstance(file, dict)]

            with db.atomic():
                File.insert_many(files).execute()
            return {"snippet_id", snippet.snippet_id}, 200
        else:
            abort(400, message="Bad posted JSON data!")

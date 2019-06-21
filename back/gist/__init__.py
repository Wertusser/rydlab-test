from gist.resources.snippets import ApiSnippet, ApiSnippetList
from gist.app import api
from gist.views import *

api.add_resource(ApiSnippetList, '/api/snippets', endpoint="api.snippets_list")
api.add_resource(ApiSnippet, '/api/snippets/<uuid:snippet_id>', endpoint="api.snippets")

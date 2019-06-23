from gist.resources.snippets import ApiSnippet, ApiSnippetList
from gist.resources.processing import UrlProcessing
from gist.app import api
from gist.views import *

api.add_resource(ApiSnippetList, '/api/snippets', endpoint="api.snippets_list")
api.add_resource(UrlProcessing, '/api/url_process/<url>', endpoint="api.url_process")
api.add_resource(ApiSnippet, '/api/snippets/<snippet_id>', endpoint="api.snippets")

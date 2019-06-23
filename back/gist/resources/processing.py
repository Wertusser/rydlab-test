from flask_restful import Resource, abort, marshal_with
from gist.fields.processing import url_processing_fields
import requests
import base64


class UrlProcessing(Resource):
    @marshal_with(url_processing_fields, envelope="result")
    def get(self, url):
        base64_url = url.replace("-", "+").replace("_", "/")
        base64_url += "=" * (4 - len(base64_url) % 4)
        url = base64.b64decode(base64_url).decode()
        r = requests.get(url)
        if r.headers['content-type'].startswith("text/plain"):
            return {"text": r.text}, 200
        else:
            abort(404, message="This is not a text file!")

from flask_restful import Resource, abort, marshal_with
from gist.fields.processing import url_processing_fields
import requests
import base64
from gist.config import max_file_size


class UrlProcessing(Resource):
    @marshal_with(url_processing_fields, envelope="result")
    def get(self, url):
        base64_url = url.replace("-", "+").replace("_", "/")
        base64_url += "=" * (4 - len(base64_url) % 4)
        url = base64.b64decode(base64_url).decode()
        r = requests.get(url)
        if r.headers['content-type'].startswith("text/plain"):
            text = r.text[:max_file_size]
            return {"text": text}, 200
        else:
            abort(400, message="This is not a text file!")

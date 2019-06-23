from flask_restful import Resource, abort
import requests


class UrlProcessing(Resource):
    def post(self, url):
        r = requests.get(url)
        if r.headers['content-type'].startswith("text/plain"):
            return r.text, 200
        else:
            abort(404, message="This is not a text file!")

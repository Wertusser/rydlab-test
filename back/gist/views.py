from gist.app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/snippet/<uuid:snippet_id>")
def snippet(snippet_id):
    return render_template("snippets.html", snippet_id=snippet_id)


@app.route("/create")
def create():
    return render_template("create.html")

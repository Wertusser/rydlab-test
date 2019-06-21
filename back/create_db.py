from gist.app import db
from gist.models import Snippet, File

with db:
    db.create_tables([Snippet, File])

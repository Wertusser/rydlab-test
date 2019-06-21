from peewee import *
from gist.app import db


class BaseModel(Model):
    class Meta:
        database = db


class Snippet(BaseModel):
    snippet_id = UUIDField(primary_key=True, unique=True)
    title = CharField()
    description = TextField()
    created_at = DateField()
    is_public = BooleanField()


class File(BaseModel):
    snippet = ForeignKeyField(Snippet, backref='snippets')
    filename = CharField()
    text = TextField()
    extension = CharField()
    is_binary = BooleanField()

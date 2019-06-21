from peewee import *
from gist.app import db
from uuid import uuid4
from datetime import datetime


class BaseModel(Model):
    class Meta:
        database = db


class Snippet(BaseModel):
    snippet_id = UUIDField(unique=True, default=uuid4)
    title = CharField()
    description = TextField()
    created_at = DateTimeField(default=datetime.now)
    is_public = BooleanField()


class File(BaseModel):
    snippet = ForeignKeyField(Snippet, backref='files')
    filename = CharField()
    text = TextField()
    extension = CharField()
    is_binary = BooleanField()

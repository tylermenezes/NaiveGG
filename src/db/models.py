#!/usr/bin/env python2

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime
import os

db = SqliteExtDatabase(os.path.dirname(os.path.realpath(__file__))+'/corpus.db')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Tweet(BaseModel):
    id = BigIntegerField(unique=True)
    mentioning = CharField()
    screen_name = CharField()
    text = TextField()
    created_at = DateTimeField(null=True)
    ingested_at = DateTimeField(default=datetime.datetime.now)
    classification = CharField(null=True)


#db.create_tables([Tweet])

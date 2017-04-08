from peewee import *
from const import DATA_BASE_NAME


class Language(Model):
    language = CharField(max_length=32)

    class Meta:
        database = SqliteDatabase(DATA_BASE_NAME)

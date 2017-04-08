from peewee import *
from const import DATA_BASE_NAME


class Status(Model):
    status = CharField(max_length=64)

    class Meta:
        database = SqliteDatabase(DATA_BASE_NAME)

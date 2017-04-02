from const import DATA_BASE_NAME
from peewee import *

db = SqliteDatabase(DATA_BASE_NAME)


class Person(Model):
    name = CharField(null=True)
    birthday = DateField(null=True)
    vacation = CharField(null=True)
    image = CharField(null=True)
    language = CharField(null=True)
    info = TextField(null=True)

    class Meta:
        database = db

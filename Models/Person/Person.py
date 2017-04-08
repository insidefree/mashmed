from Models.Person.Language import Language
from const import DATA_BASE_NAME
from peewee import *

db = SqliteDatabase(DATA_BASE_NAME)


class Person(Model):
    first_name = CharField(null=True)
    second_name = CharField(null=True)
    birthday = DateField(null=True)
    image = CharField(null=True)
    language = ForeignKeyField(Language)
    info = TextField(null=True)

    class Meta:
        database = db

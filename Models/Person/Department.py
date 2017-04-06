from const import DATA_BASE_NAME
from Models.Person.Doctor import Doctor
from peewee import *

db = SqliteDatabase(DATA_BASE_NAME)


class Department(Model):
    doctor = ForeignKeyField(Doctor, related_name='department')
    title = CharField(max_length=64)

    class Meta:
        database = db

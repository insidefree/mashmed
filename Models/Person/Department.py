from const import DATA_BASE_NAME
from peewee import *

db = SqliteDatabase(DATA_BASE_NAME)


class Department(Model):
    department_title = CharField(max_length=64)

    class Meta:
        database = db

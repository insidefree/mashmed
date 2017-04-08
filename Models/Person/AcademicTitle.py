from peewee import *
from const import DATA_BASE_NAME

db = SqliteDatabase(DATA_BASE_NAME)


class AcademicTitle(Model):
    academic_title = CharField(max_length=64)

    def __repr__(self):
        return self.academic_title

    def __str__(self):
        print(f'{self.academic_title}')
        return 'asd'

    class Meta:
        database = db

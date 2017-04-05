from peewee import *
from Models.Person.Person import Person


class Doctor(Person):
    department = CharField(null=True)
    subDepartment = CharField(null=True)
    visible_tg = BooleanField(null=True)
    status = CharField(null=True)
    first_tg = CharField(null=True)
    link = CharField(null=True)
    academic_title = CharField(null=True)



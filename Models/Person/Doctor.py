from peewee import *

from Models.Person.Status import Status
from Models.Person.Person import Person
from Models.Person.Department import Department
from Models.Person.AcademicTitle import AcademicTitle
from Models.Person.SubDepartment import SubDepartment
from const import DATA_BASE_NAME


class Doctor(Person):
    department = ForeignKeyField(Department, null=True)
    sub_department = ForeignKeyField(SubDepartment, null=True)
    visible_tg = BooleanField(null=True)
    status = ForeignKeyField(Status, null=True)
    first_tg = CharField(null=True)
    link = CharField(null=True)
    academic_title = ForeignKeyField(AcademicTitle, null=True)

    @staticmethod
    def get_doctors_from_db():
        for doctor in Doctor.select():
            print(f'{doctor.first_name}')

    class Meta:
        database = SqliteDatabase(DATA_BASE_NAME)

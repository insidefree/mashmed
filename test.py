# from const import DATA_BASE_NAME
# from peewee import *
# from datetime import date
#
# db = SqliteDatabase(DATA_BASE_NAME)
#
#
# class Person(Model):
#     name = CharField()
#     birthday = DateField()
#     is_relative = BooleanField()
#
#     class Meta:
#         database = db  # модель будет использовать базу данных 'people.db'
#
#
# class Pet(Model):
#     owner = ForeignKeyField(Person, related_name='pets')
#     name = CharField()
#     animal_type = CharField()
#
#     class Meta:
#         database = db  # модель будет использовать базу данных 'people.db'
#
#
# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
# uncle_bob.save()
#
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
#
# bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
# herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
# herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
# herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
#
from Models.Person.AcademicTitle import AcademicTitle

at = AcademicTitle('asd')
print(at)
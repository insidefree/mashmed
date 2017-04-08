from const import DATA_BASE_NAME
from playhouse.migrate import *
from Models.Person.Department import Department

my_db = SqliteDatabase(DATA_BASE_NAME)
migrator = SqliteMigrator(my_db)

department = ForeignKeyField(Department, to_field='id', related_name='departments', null=True)

migrate(
    migrator.drop_column('doctor', 'vacation'),
    migrator.drop_column('doctor', 'status')
)

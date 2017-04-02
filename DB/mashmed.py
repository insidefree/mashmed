from Models.Person.Person import Person


class DB:
    def __init__(self, class_name):
        self.class_name = class_name

    def create_table(self):
        self.class_name.create_table()

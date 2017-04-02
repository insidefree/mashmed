from datetime import date
from Models.Person.Doctor import Doctor
from Assuta.AssutaOld import AssutaOld
from Assuta.Assuta import Assuta


def main():
    # Doctor.create_table()
    # uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), vacation='developer')
    # doctor = Doctor(name='Bob', birthday=date(1960, 1, 15), vacation='developer', department='lor2')
    # doctor.save()
    asold = AssutaOld()
    # asold.print_doctors_info()
    asold.save_doctors()

if __name__ == '__main__':
    main()

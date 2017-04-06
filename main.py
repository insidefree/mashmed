from datetime import date
from Models.Person.Doctor import Doctor
from Assuta.AssutaOld import AssutaOld
from Assuta.Assuta import Assuta


def main():
    # asold = AssutaOld()
    # asold.save_doctors()
    Doctor.get_doctors_from_db()

if __name__ == '__main__':
    main()

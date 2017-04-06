from datetime import date
from Models.Person.Doctor import Doctor
from Assuta.AssutaOld import AssutaOld
from Assuta.Assuta import Assuta
from Assuta.AssutaNew import AssutaNew


def main():
    # asold = AssutaOld()
    # asold.save_doctors()
    # Doctor.get_doctors_from_db()
    assuta_new = AssutaNew()
    assuta_new.sing_in()
    assuta_new.fill_doctors_info()

    assuta_new.session_end()


if __name__ == '__main__':
    main()

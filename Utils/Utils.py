from const import ACADEMIC_TITLE_DIC

from Models.Person.Department import Department

dep = Department()


class Utils:
    @staticmethod
    def remove_blank_lines(lines):
        return "".join([s for s in lines.strip().splitlines(True) if s.strip("\r\n").strip()])

    @staticmethod
    def handle_academic_title(academic_title):
        if academic_title in ACADEMIC_TITLE_DIC:
            return ACADEMIC_TITLE_DIC[academic_title]
        else:
            return academic_title if academic_title != '' else None

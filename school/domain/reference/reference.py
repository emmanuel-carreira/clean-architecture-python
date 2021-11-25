from datetime import datetime

from school.domain.student.student import Student


class Reference:
    def __init__(self, indicated_student: Student, indicator_student: Student) -> None:
        self.indicated_student = indicated_student
        self.indicator_student = indicator_student
        self.reference_date = datetime.utcnow()

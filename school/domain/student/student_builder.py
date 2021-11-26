from school.domain.cpf import CPF
from school.domain.phone import Phone
from school.domain.student.student import Student


class StudentBuilder:
    def __init__(self) -> None:
        self.student = None
        self.student_created = False

    def with_cpf_email_and_name(self, cpf: str, email: str, name: str):
        if self.student_created:
            raise ValueError("Student already created!")
        self.student_created = True
        self.student = Student(CPF(cpf), email, name)
        return self

    def with_phone(self, ddd: str, number: str):
        if not self.student:
            raise AttributeError("Student has not been set yet")
        self.student.add_phone(Phone(ddd, number))
        return self

    def create(self):
        self.student_created = False
        return self.student

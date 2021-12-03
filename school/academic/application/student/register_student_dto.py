from dataclasses import dataclass

from school.academic.domain.student.student import Student
from school.academic.domain.student.student_builder import StudentBuilder


@dataclass
class RegisterStudentDTO:
    cpf: str
    email: str
    name: str

    def create_student(self) -> Student:
        student_builder = StudentBuilder()
        return student_builder.with_cpf_email_and_name(self.cpf, self.email, self.name).create()
    
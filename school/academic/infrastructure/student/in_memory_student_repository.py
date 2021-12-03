from typing import List

from school.academic.domain.student.student_not_found import StudentNotFound
from school.academic.domain.student.student_repository import StudentRepository
from school.academic.domain.student.student import Student
from school.shared.domain.cpf import CPF


class InMemoryStudentRepository(StudentRepository):
    def __init__(self) -> None:
        super().__init__()
        self.students = []

    def list_all_registered_students(self) -> List[Student]:
        return self.students

    def register(self, student: Student) -> None:
        self.students.append(student)

    def search_by_cpf(self, cpf: CPF) -> Student:
        for student in self.students:
            if student.cpf == cpf:
                return student
        raise StudentNotFound(cpf)

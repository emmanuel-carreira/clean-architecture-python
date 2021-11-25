from typing import List

from school.domain.cpf import CPF
from school.domain.student.student import Student


class StudentRepository:
    def list_all_registered_students(self) -> List[Student]:
        raise NotImplementedError

    def register(self, student: Student) -> None:
        raise NotImplementedError

    def search_by_cpf(self, cpf: CPF) -> Student:
        raise NotImplementedError

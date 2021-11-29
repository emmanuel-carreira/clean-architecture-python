import unittest

from school.application.student.register_student import RegisterStudent
from school.application.student.register_student_dto import RegisterStudentDTO
from school.domain.cpf import CPF
from school.infrastructure.student.in_memory_student_repository import InMemoryStudentRepository


class RegisterStudentTest(unittest.TestCase):
    def test_student_should_be_persisted(self):
        repository = InMemoryStudentRepository()
        self.assertEqual(repository.list_all_registered_students(), [])

        student_data = RegisterStudentDTO(cpf="123.456.789-00", email="test@test.com", name="Test")
        register_student = RegisterStudent(repository)
        register_student.execute(student_data)

        self.assertIsNotNone(repository.search_by_cpf(CPF("123.456.789-00")))
        registered_student = repository.search_by_cpf(CPF("123.456.789-00"))
        self.assertEqual(registered_student.email, "test@test.com")
        self.assertEqual(registered_student.name, "Test")

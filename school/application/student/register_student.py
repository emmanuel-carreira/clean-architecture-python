from school.application.student.register_student_dto import RegisterStudentDTO
from school.domain.student.student_repository import StudentRepository


class RegisterStudent:
    def __init__(self, repository: StudentRepository) -> None:
        self.repository = repository

    def execute(self, student_data: RegisterStudentDTO) -> None:
        student = student_data.create_student()
        self.repository.register(student)

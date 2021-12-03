from school.application.student.register_student_dto import RegisterStudentDTO
from school.domain.event_publisher import EventPublisher
from school.domain.student.registered_student_event import RegisteredStudentEvent
from school.domain.student.student_repository import StudentRepository


class RegisterStudent:
    def __init__(self, repository: StudentRepository, publisher: EventPublisher) -> None:
        self.repository = repository
        self.publisher = publisher

    def execute(self, student_data: RegisterStudentDTO) -> None:
        student = student_data.create_student()
        self.repository.register(student)
        self.publisher.publish(RegisteredStudentEvent(student.cpf))

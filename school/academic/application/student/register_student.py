from school.academic.application.student.register_student_dto import RegisterStudentDTO
from school.academic.domain.student.registered_student_event import RegisteredStudentEvent
from school.academic.domain.student.student_repository import StudentRepository
from school.shared.domain.event.event_publisher import EventPublisher


class RegisterStudent:
    def __init__(self, repository: StudentRepository, publisher: EventPublisher) -> None:
        self.repository = repository
        self.publisher = publisher

    def execute(self, student_data: RegisterStudentDTO) -> None:
        student = student_data.create_student()
        self.repository.register(student)
        self.publisher.publish(RegisteredStudentEvent(student.cpf))

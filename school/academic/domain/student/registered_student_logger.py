import logging

from school.academic.domain.student.registered_student_event import RegisteredStudentEvent
from school.academic.domain.event_subscriber import EventSubscriber
from school.academic.domain.event import Event


class RegisteredStudentLogger(EventSubscriber):
    def execute(self, event: RegisteredStudentEvent):
        logging.info(
            "Student with CPF %s was registered in %s",
            event.student_cpf, event.moment.isoformat()
        )

    def should_handle(self, event: Event):
        return isinstance(event, RegisteredStudentEvent)

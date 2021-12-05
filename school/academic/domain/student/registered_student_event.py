from datetime import datetime

from school.shared.domain.cpf import CPF
from school.shared.domain.event.event_type import EventType
from school.shared.domain.event.event import Event


class RegisteredStudentEvent(Event):
    def __init__(self, student_cpf: CPF) -> None:
        self._student_cpf = student_cpf
        self._moment = datetime.utcnow()

    @property
    def event_type(self) -> EventType:
        return EventType.REGISTERED_STUDENT

    @property
    def infos(self) -> dict:
        return {"student_cpf": self.student_cpf}

    @property
    def moment(self) -> datetime:
        return self._moment

    @property
    def student_cpf(self) -> CPF:
        return self._student_cpf

from datetime import datetime

from school.academic.domain.cpf import CPF
from school.academic.domain.event import Event


class RegisteredStudentEvent(Event):
    def __init__(self, student_cpf: CPF) -> None:
        self._student_cpf = student_cpf
        self._moment = datetime.utcnow()

    @property
    def student_cpf(self) -> CPF:
        return self._student_cpf

    @property
    def moment(self) -> datetime:
        return self._moment

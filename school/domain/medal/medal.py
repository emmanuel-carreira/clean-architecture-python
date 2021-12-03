from school.domain.cpf import CPF


class Medal:
    def __init__(self, student_cpf: CPF, name: str) -> None:
        self._student_cpf = student_cpf
        self._name = name

    @property
    def student_cpf(self):
        return self._student_cpf

    @property
    def name(self):
        return self._name

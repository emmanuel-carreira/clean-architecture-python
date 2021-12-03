from school.domain.cpf import CPF


class Medal:
    def __init__(self, student_cpf: CPF, name: str) -> None:
        self.student_cpf = student_cpf
        self.name = name

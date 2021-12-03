from school.academic.domain.cpf import CPF


class StudentNotFound(Exception):
    def __init__(self, cpf: CPF, *args) -> None:
        super().__init__(cpf, *args)
        self.cpf = cpf

    def __str__(self) -> str:
        return f"Student with CPF {self.cpf} not found!"
        
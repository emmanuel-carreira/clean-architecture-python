from school.domain.cpf import CPF
from school.domain.medal.medal import Medal


class MedalRepository:
    def add_medal(self, medal: Medal):
        raise NotImplementedError

    def list_student_medals(self, student_cpf: CPF):
        raise NotImplementedError

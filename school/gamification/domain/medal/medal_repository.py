from typing import List

from school.academic.domain.cpf import CPF
from school.gamification.domain.medal.medal import Medal


class MedalRepository:
    def add_medal(self, medal: Medal) -> None:
        raise NotImplementedError

    def list_student_medals(self, student_cpf: CPF) -> List[Medal]:
        raise NotImplementedError

from typing import List

from school.gamification.domain.medal.medal import Medal
from school.shared.domain.cpf import CPF


class MedalRepository:
    def add_medal(self, medal: Medal) -> None:
        raise NotImplementedError

    def list_student_medals(self, student_cpf: CPF) -> List[Medal]:
        raise NotImplementedError

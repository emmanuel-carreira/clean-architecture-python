from typing import List

from school.academic.domain.cpf import CPF
from school.gamification.domain.medal.medal import Medal
from school.gamification.domain.medal.medal_repository import MedalRepository


class InMemoryMedalRepository(MedalRepository):
    def __init__(self) -> None:
        self.medals = {}

    def add_medal(self, medal: Medal) -> None:
        student_cpf_number = medal.student_cpf.number
        if student_cpf_number in self.medals:
            self.medals[student_cpf_number].append(medal)
        else:
            self.medals[student_cpf_number] = [medal]

    def list_student_medals(self, student_cpf: CPF) -> List[Medal]:
        return self.medals.get(student_cpf.number, [])

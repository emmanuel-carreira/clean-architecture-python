from school.domain.medal.medal import Medal
from school.domain.medal.medal_repository import MedalRepository


class InMemoryMedalRepository(MedalRepository):
    def __init__(self) -> None:
        self.medals = {}

    def add_medal(self, medal: Medal) -> None:
        student_cpf = medal.student_cpf.number
        if student_cpf in self.medals:
            self.medals[student_cpf].append(medal)
        else:
            self.medals[student_cpf] = [medal]

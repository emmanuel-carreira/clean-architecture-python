from school.gamification.domain.medal.medal_repository import MedalRepository
from school.gamification.domain.medal.medal import Medal
from school.shared.domain.event.event_subscriber import EventSubscriber
from school.shared.domain.event.event_type import EventType
from school.shared.domain.event.event import Event


class GenerateMedalNewStudent(EventSubscriber):
    def __init__(self, repository: MedalRepository) -> None:
        self.repository = repository

    def execute(self, event: Event):
        student_cpf = event.infos.get("student_cpf")
        medal = Medal(student_cpf, "NEW")
        self.repository.add_medal(medal)

    def should_handle(self, event: Event):
        return event.event_type == EventType.REGISTERED_STUDENT

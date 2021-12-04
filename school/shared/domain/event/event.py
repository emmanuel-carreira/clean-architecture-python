from datetime import datetime

from school.shared.domain.event.event_type import EventType


class Event:
    @property
    def event_type(self) -> EventType:
        raise NotImplementedError

    @property
    def infos(self) -> dict:
        raise NotImplementedError

    @property
    def moment(self) -> datetime:
        raise NotImplementedError

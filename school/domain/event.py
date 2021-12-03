from datetime import datetime


class Event:
    @property
    def moment(self) -> datetime:
        raise NotImplementedError

from school.shared.domain.event.event import Event
from school.shared.domain.event.event_subscriber import EventSubscriber


class EventPublisher:
    def __init__(self) -> None:
        self.subscribers = []

    def publish(self, event: Event):
        for subscriber in self.subscribers:
            subscriber.handle_event(event)

    def subscribe(self, subscriber: EventSubscriber):
        self.subscribers.append(subscriber)

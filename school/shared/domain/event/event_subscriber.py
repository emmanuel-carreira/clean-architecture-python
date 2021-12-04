from school.shared.domain.event.event import Event


class EventSubscriber:
    def handle_event(self, event: Event):
        if self.should_handle(event):
            self.execute(event)

    def execute(self, event: Event):
        raise NotImplementedError

    def should_handle(self, event: Event):
        raise NotImplementedError

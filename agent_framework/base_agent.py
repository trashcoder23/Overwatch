from abc import ABC, abstractmethod


class BaseAgent(ABC):
    def __init__(self, name, event_bus):
        self.name = name
        self.event_bus = event_bus

    def send_event(self, target_agent, event_type, data):
        """Send event to another agent"""
        event = {
            "source": self.name,
            "target": target_agent,
            "type": event_type,
            "data": data
        }

        self.event_bus.publish(event)

    def receive_event(self, event):
        """Receive events from event bus"""
        if event["target"] == self.name:
            self.handle_event(event)

    @abstractmethod
    def handle_event(self, event):
        """Each agent defines how it handles events"""
        pass
import datetime


class BaseAgent:

    def __init__(self, name, registry):
        self.name = name
        self.registry = registry

    def send(self, target, event_type, data):

        agent = self.registry.get(target)

        if not agent:
            print(f"[ERROR] Agent {target} not found")
            return

        event = {
            "source": self.name,
            "target": target,
            "type": event_type,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "incident_id": getattr(data, "id", None),
            "data": data
        }

        print(f"[A2A] {self.name} → {target} ({event_type})")

        agent.receive(event)

    def receive(self, event):
        self.handle_event(event)

    def handle_event(self, event):
        pass
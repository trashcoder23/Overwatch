class BaseAgent:

    def __init__(self, name, registry):

        self.name = name
        self.registry = registry

    def send(self, target, event_type, data):

        agent = self.registry.get(target)

        if agent:

            print(f"[A2A] {self.name} → {target} ({event_type})")

            agent.receive({
                "source": self.name,
                "type": event_type,
                "data": data
            })

    def receive(self, event):

        self.handle_event(event)

    def handle_event(self, event):
        pass

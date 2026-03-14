class EventBus:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, agent):
        self.subscribers.append(agent)

    def publish(self, event):
        print(f"[EVENT BUS] {event['source']} → {event['target']} ({event['type']})")

        for agent in self.subscribers:
            agent.receive_event(event)
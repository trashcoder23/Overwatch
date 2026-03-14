from agent_framework.event_bus import EventBus


class AgentOrchestrator:

    def __init__(self):
        self.event_bus = EventBus()
        self.agents = {}

    def register_agent(self, agent):
        self.agents[agent.name] = agent
        self.event_bus.subscribe(agent)

    def send_initial_event(self, target_agent, event_type, data):
        event = {
            "source": "orchestrator",
            "target": target_agent,
            "type": event_type,
            "data": data
        }

        self.event_bus.publish(event)

    def list_agents(self):
        print("Registered agents:")
        for name in self.agents:
            print("-", name)
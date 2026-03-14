from agent_framework.agent_registry import AgentRegistry

from agents.sentry_agent import SentryAgent
from agents.diagnostician_agent import DiagnosticianAgent
from agents.strategist_agent import StrategistAgent
from agents.logistics_agent import LogisticsAgent
from agents.orchestrator_agent import OrchestratorAgent


def main():

    registry = AgentRegistry()

    sentry = SentryAgent(registry)
    diagnostician = DiagnosticianAgent(registry)
    strategist = StrategistAgent(registry)
    logistics = LogisticsAgent(registry)
    orchestrator = OrchestratorAgent(registry)

    registry.register(sentry)
    registry.register(diagnostician)
    registry.register(strategist)
    registry.register(logistics)
    registry.register(orchestrator)

    print("Registered agents:")

    for agent in registry.all():
        print("-", agent.name)

    print("\nStarting Sentry monitoring...\n")

    sentry.monitor()


if __name__ == "__main__":
    main()

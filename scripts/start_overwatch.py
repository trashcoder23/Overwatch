from agent_framework.agent_orchestrator import AgentOrchestrator

from agents.sentry_agent import SentryAgent
from agents.diagnostician_agent import DiagnosticianAgent
from agents.strategist_agent import StrategistAgent
from agents.logistics_agent import LogisticsAgent


def main():

    orchestrator = AgentOrchestrator()

    sentry = SentryAgent(orchestrator.event_bus)
    diagnostician = DiagnosticianAgent(orchestrator.event_bus)
    strategist = StrategistAgent(orchestrator.event_bus)
    logistics = LogisticsAgent(orchestrator.event_bus)

    orchestrator.register_agent(sentry)
    orchestrator.register_agent(diagnostician)
    orchestrator.register_agent(strategist)
    orchestrator.register_agent(logistics)

    orchestrator.list_agents()

    print("\nStarting Sentry monitoring...\n")

    sentry.monitor()


if __name__ == "__main__":
    main()
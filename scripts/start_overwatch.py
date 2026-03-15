from agent_framework.agent_registry import AgentRegistry

from agents.sentry_agent import SentryAgent
from agents.diagnostician_agent import DiagnosticianAgent
from agents.strategist_agent import StrategistAgent
from agents.logistics_agent import LogisticsAgent
from agents.traffic_controller_agent import TrafficControllerAgent

from agent_framework.agent_orchestrator import AgentOrchestrator


def main():

    print("\n========== OVERWATCH AGENT SYSTEM ==========\n")

    registry = AgentRegistry()

    # Create agents

    sentry = SentryAgent(registry)
    diagnostician = DiagnosticianAgent(registry)
    strategist = StrategistAgent(registry)
    logistics = LogisticsAgent(registry)
    orchestrator = AgentOrchestrator(registry)
    traffic = TrafficControllerAgent(registry)

    # Register agents

    registry.register(sentry)
    registry.register(diagnostician)
    registry.register(strategist)
    registry.register(logistics)
    registry.register(orchestrator)
    registry.register(traffic)

    print("Registered agents:\n")

    for agent in registry.all():
        print(f" - {agent.name}")

    print("\n===========================================\n")

    # Manual MCP test (optional)

    test = input("Run MCP infrastructure test? (yes/no): ")

    if test.lower() == "yes":

        print("\n[MCP TEST] Simulating failover strategy\n")

        from agent_framework.incident import Incident

        incident = Incident(
            source="manual_test",
            metrics={"reason": "demo"}
        )

        incident.set_strategy("failover_region")

        logistics.handle_event({
            "type": "execute_strategy",
            "data": incident
        })

        print("\n[MCP TEST COMPLETE]\n")

    # Start monitoring loop

    print("Starting Sentry monitoring...\n")

    sentry.monitor()


if __name__ == "__main__":
    main()
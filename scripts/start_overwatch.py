from agent_framework.agent_registry import AgentRegistry

from agents.sentry_agent import SentryAgent
from agents.diagnostician_agent import DiagnosticianAgent
from agents.strategist_agent import StrategistAgent
from agents.logistics_agent import LogisticsAgent
from agent_framework.agent_orchestrator import AgentOrchestrator

import threading
import time


def start_monitoring(sentry):
    sentry.monitor()


def main():

    registry = AgentRegistry()

    # Initialize Agents
    sentry = SentryAgent(registry)
    diagnostician = DiagnosticianAgent(registry)
    strategist = StrategistAgent(registry)
    logistics = LogisticsAgent(registry)
    orchestrator = AgentOrchestrator(registry)

    # Register Agents
    registry.register(sentry)
    registry.register(diagnostician)
    registry.register(strategist)
    registry.register(logistics)
    registry.register(orchestrator)

    print("\nRegistered agents:")

    for agent in registry.all():
        print("-", agent.name)

    print("\nStarting Overwatch system...\n")

    # Start Sentry Monitoring in Background
    monitoring_thread = threading.Thread(
        target=start_monitoring,
        args=(sentry,),
        daemon=True
    )

    monitoring_thread.start()

    print("[SYSTEM] Sentry monitoring started")

    # Keep main process alive
    try:

        while True:
            time.sleep(5)

    except KeyboardInterrupt:

        print("\n[SYSTEM] Shutting down Overwatch...")


if __name__ == "__main__":
    main()
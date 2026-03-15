from agent_framework.base_agent import BaseAgent

# MCP tools
from mcp.tools.restart_service import restart_service
from mcp.tools.deploy_container import deploy_container
from mcp.tools.switch_traffic import switch_to_region


class LogisticsAgent(BaseAgent):

    def __init__(self, registry):

        super().__init__("Logistics", registry)

    def handle_event(self, event):

        if event["type"] == "execute_strategy":

            incident = event["data"]

            print("\n[LOGISTICS] executing recovery strategy")

            strategy = incident.strategy

            print(f"[LOGISTICS] strategy → {strategy}")

            try:

                if strategy == "restart_service":

                    print("[LOGISTICS] restarting container app")

                    restart_service("demo-service-east")

                elif strategy == "scale_service":

                    print("[LOGISTICS] scaling service")

                    deploy_container("demo-service-east")

                elif strategy == "failover_region":

                    print("[LOGISTICS] triggering regional failover")

                    switch_to_region("west")

                elif strategy == "rollback_deployment":

                    print("[LOGISTICS] rollback not implemented yet")

                else:

                    print("[LOGISTICS] unknown strategy → manual investigation required")

            except Exception as e:

                print("[LOGISTICS] execution failed:", str(e))

                return

            incident.resolve()

            print("[LOGISTICS] INCIDENT RESOLVED")

            print("[LOGISTICS] FINAL INCIDENT STATE →")

            print(incident.to_dict())
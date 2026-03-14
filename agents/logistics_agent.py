from agent_framework.base_agent import BaseAgent


class LogisticsAgent(BaseAgent):

    def __init__(self, registry):

        super().__init__("Logistics", registry)

    def handle_event(self, event):

        if event["type"] == "execute_strategy":

            incident = event["data"]

            print("[LOGISTICS] executing recovery action...")

            if incident.strategy == "restart_service":

                print("[LOGISTICS] restarting service...")

            elif incident.strategy == "scale_service":

                print("[LOGISTICS] scaling resources...")

            elif incident.strategy == "failover_region":

                print("[LOGISTICS] initiating regional failover...")

            else:

                print("[LOGISTICS] manual investigation required")

            incident.resolve()

            print("[LOGISTICS] INCIDENT RESOLVED →", incident.to_dict())

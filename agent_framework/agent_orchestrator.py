from agent_framework.base_agent import BaseAgent


class OrchestratorAgent(BaseAgent):

    def __init__(self, registry):

        super().__init__("Orchestrator", registry)

    def handle_event(self, event):

        if event["type"] == "strategy_ready":

            incident = event["data"]

            print("\n[ORCHESTRATOR] recovery plan generated")

            print("[ORCHESTRATOR] PLAN →", incident.to_dict())

            decision = input("\nApprove execution? (yes/no): ")

            if decision.lower() == "yes":

                print("[ORCHESTRATOR] executing recovery plan")

                self.send("Logistics", "execute_strategy", incident)

            else:

                print("[ORCHESTRATOR] execution aborted")

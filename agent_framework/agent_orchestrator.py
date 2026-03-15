from agent_framework.base_agent import BaseAgent


class AgentOrchestrator(BaseAgent):

    def __init__(self, registry):
        super().__init__("Orchestrator", registry)

    def handle_event(self, event):

        if event["type"] == "strategy_ready":

            incident = event["data"]

            print("\n[ORCHESTRATOR] Recovery plan generated")
            print("[ORCHESTRATOR] PLAN →", incident.to_dict())

            confidence = incident.confidence or 0.5

            if confidence > 0.85:

                print("[ORCHESTRATOR] High confidence strategy. Auto approving.")
                self.send("Logistics", "execute_strategy", incident)

            elif confidence > 0.6:

                decision = input("\nApprove execution? (yes/no): ")

                if decision.lower() == "yes":
                    print("[ORCHESTRATOR] executing recovery plan")
                    self.send("Logistics", "execute_strategy", incident)
                else:
                    print("[ORCHESTRATOR] execution aborted")

            else:

                print("[ORCHESTRATOR] Low confidence strategy.")
                print("[ORCHESTRATOR] Manual investigation recommended.")
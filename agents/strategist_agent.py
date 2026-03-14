from agent_framework.base_agent import BaseAgent


class StrategistAgent(BaseAgent):

    def __init__(self, event_bus):
        super().__init__("Strategist", event_bus)

    def handle_event(self, event):

        if event["type"] == "incident_classified":

            print("[STRATEGIST] evaluating recovery strategy...")

            incident = event["data"]

            classification = incident.classification
            action = incident.recommended_action

            decision = None

            if action == "restart_service":
                decision = "self_heal_restart"

            elif action == "scale_service":
                decision = "self_heal_scale"

            elif classification == "service_down":
                decision = "failover_region"

            else:
                decision = "manual_investigation"

            incident.set_strategy(decision)

            print("[STRATEGIST] STRATEGY DECISION →", incident.to_dict())

            self.send_event(
                "Logistics",
                "execute_strategy",
                incident
            )
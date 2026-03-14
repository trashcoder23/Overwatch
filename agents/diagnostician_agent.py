from agent_framework.base_agent import BaseAgent
from foundry.model_client import FoundryClient


class DiagnosticianAgent(BaseAgent):

    def __init__(self, event_bus):

        super().__init__("Diagnostician", event_bus)

        self.ai = FoundryClient(
            endpoint="YOUR_FOUNDRY_ENDPOINT",
            model="YOUR_MODEL_NAME"
        )

    def handle_event(self, event):

        if event["type"] == "incident_detected":

            incident = event["data"]

            print("[DIAGNOSTICIAN] analyzing incident with AI...")

            prompt = f"""
            Analyze this incident:

            Metrics:
            {incident.metrics}

            Determine the root cause and recommended action.
            """

            ai_response = self.ai.ask(prompt)

            print("[DIAGNOSTICIAN AI RESPONSE]")
            print(ai_response)

            # simple fallback parsing for now
            if "scale_service" in ai_response:
                classification = "performance_issue"
                action = "scale_service"

            elif "restart_service" in ai_response:
                classification = "service_failure"
                action = "restart_service"

            else:
                classification = "unknown"
                action = "investigate"

            incident.update_classification(classification, action)

            print("[DIAGNOSTICIAN] RCA REPORT →", incident.to_dict())

            self.send_event(
                "Strategist",
                "incident_classified",
                incident
            )
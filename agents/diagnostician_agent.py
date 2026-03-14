from agent_framework.base_agent import BaseAgent
from foundry.model_client import FoundryClient
import json
import re


def extract_json(response_text):

    try:
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)

        if json_match:
            return json.loads(json_match.group())

    except Exception:
        pass

    return None


class DiagnosticianAgent(BaseAgent):

    def __init__(self, event_bus):

        super().__init__("Diagnostician", event_bus)

        self.ai = FoundryClient()

        with open("foundry/prompts/diagnostician_instruction.txt") as f:
            self.instruction = f.read()

    def handle_event(self, event):

        if event["type"] == "incident_detected":

            print("[DIAGNOSTICIAN] analyzing incident with AI...")

            incident = event["data"]

            prompt = f"""
Incident Context:

Service State:
{incident.metrics.get("service_state", "unknown")}

Metrics:
{incident.metrics}

System Information:
- Environment: production
- Service: demo-app
- Monitoring agent: Sentry

Analyze the incident and return the JSON response.
"""

            ai_response = self.ai.ask(self.instruction, prompt)

            print("[AI RCA RAW RESPONSE]")
            print(ai_response)

            result = extract_json(ai_response)

            if result:

                classification = result.get("classification", "unknown")
                action = result.get("recommended_action", "investigate")

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
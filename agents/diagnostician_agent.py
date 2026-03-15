from agent_framework.base_agent import BaseAgent
from foundry.model_client import FoundryClient
import json
import re


def extract_json(text):
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass
    return None


class DiagnosticianAgent(BaseAgent):

    def __init__(self, registry):
        super().__init__("Diagnostician", registry)

        self.ai = FoundryClient()

        with open("foundry/prompts/diagnostician_instruction.txt") as f:
            self.instruction = f.read()

    def handle_event(self, event):

        if event["type"] == "incident_detected":

            incident = event["data"]

            print("[DIAGNOSTICIAN] analyzing incident with AI...")

            prompt = f"""
Incident metrics:
{incident.metrics}
"""

            ai_response = self.ai.ask(self.instruction, prompt)

            print("[AI RCA RAW RESPONSE]")
            print(ai_response)

            result = extract_json(ai_response)

            if result:
                classification = result.get("classification", "unknown")
                action = result.get("recommended_action", "investigate")

                confidence_map = {
                    "low": 0.3,
                    "medium": 0.6,
                    "high": 0.9
                }

                conf = result.get("confidence", "medium")

                if isinstance(conf, str):
                    confidence = confidence_map.get(conf.lower(), 0.6)
                else:
                    confidence = float(conf)

            else:
                classification = "unknown"
                action = "investigate"
                confidence = 0.5

            incident.update_classification(classification, action, confidence)

            print("[DIAGNOSTICIAN] RCA REPORT →", incident.to_dict())

            self.send("Strategist", "incident_classified", incident)
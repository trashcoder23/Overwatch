from agent_framework.base_agent import BaseAgent
from foundry.model_client import FoundryClient
import json
import re


def extract_json(response_text):

    try:
        match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        pass

    return None


class LogisticsAgent(BaseAgent):

    def __init__(self, event_bus):

        super().__init__("Logistics", event_bus)

        self.ai = FoundryClient()

        with open("foundry/prompts/logistics_instruction.txt") as f:
            self.instruction = f.read()

    def handle_event(self, event):

        if event["type"] == "execute_strategy":

            incident = event["data"]

            print("[LOGISTICS] planning recovery execution with AI...")

            prompt = f"""
Recovery Strategy: {incident.strategy}

Metrics:
{incident.metrics}

Describe the infrastructure action needed.
"""

            ai_response = self.ai.ask(self.instruction, prompt)

            print("[AI EXECUTION PLAN]")
            print(ai_response)

            print("[LOGISTICS] executing recovery action...")

            if incident.strategy == "scale_service":

                print("[LOGISTICS] scaling service resources...")

            elif incident.strategy == "restart_service":

                print("[LOGISTICS] restarting service...")

            elif incident.strategy == "failover_region":

                print("[LOGISTICS] initiating regional failover...")

            else:

                print("[LOGISTICS] manual investigation required")

            incident.resolve()

            print("[LOGISTICS] INCIDENT RESOLVED →", incident.to_dict())
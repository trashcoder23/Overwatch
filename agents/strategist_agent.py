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


class StrategistAgent(BaseAgent):

    def __init__(self, registry):

        super().__init__("Strategist", registry)

        self.ai = FoundryClient()

        with open("foundry/prompts/strategist_instruction.txt") as f:
            self.instruction = f.read()

    def handle_event(self, event):

        if event["type"] == "incident_classified":

            incident = event["data"]

            print("[STRATEGIST] generating recovery strategy with AI...")

            prompt = f"""
Incident classification: {incident.classification}

Metrics:
{incident.metrics}
"""

            ai_response = self.ai.ask(self.instruction, prompt)

            print("[AI STRATEGY RESPONSE]")
            print(ai_response)

            result = extract_json(ai_response)

            if result:
                strategy = result.get("strategy", "investigate")
            else:
                strategy = "investigate"

            incident.set_strategy(strategy)

            print("[STRATEGIST] STRATEGY →", incident.to_dict())

            self.send("Orchestrator", "strategy_ready", incident)

from agent_framework.base_agent import BaseAgent
from mcp.tools.switch_traffic import switch_to_region


class TrafficControllerAgent(BaseAgent):

    def __init__(self, registry):

        super().__init__("TrafficController", registry)

    def handle_event(self, event):

        if event["type"] == "failover_region":

            incident = event["data"]

            print("[TRAFFIC CONTROLLER] initiating regional failover")

            switch_to_region("west")

            print("[TRAFFIC CONTROLLER] traffic rerouted")
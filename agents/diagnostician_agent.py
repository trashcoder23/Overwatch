from agent_framework.base_agent import BaseAgent


class DiagnosticianAgent(BaseAgent):

    def __init__(self, event_bus):
        super().__init__("Diagnostician", event_bus)

    def handle_event(self, event):

        if event["type"] == "incident_detected":

            print("[DIAGNOSTICIAN] analyzing incident...")

            incident = event["data"]
            metrics = incident.metrics

            classification = "unknown"
            recommended_action = "investigate"

            if "latency_ms" in metrics:

                latency = metrics["latency_ms"]
                error_rate = metrics["error_rate"]

                if latency > 2000 or error_rate > 0.15:
                    classification = "severe_performance_issue"
                    recommended_action = "scale_service"

                elif error_rate > 0.1:
                    classification = "performance_issue"
                    recommended_action = "scale_service"

            incident.update_classification(classification, recommended_action)

            print("[DIAGNOSTICIAN] RCA REPORT →", incident.to_dict())

            self.send_event(
                "Strategist",
                "incident_classified",
                incident
            )
import requests
import time
from agent_framework.base_agent import BaseAgent
from agent_framework.incident import Incident


APP_URL = "http://127.0.0.1:8000"


class SentryAgent(BaseAgent):

    def __init__(self, event_bus):
        super().__init__("Sentry", event_bus)

    def monitor(self):

        while True:
            try:
                health = requests.get(f"{APP_URL}/health")

                if health.status_code != 200:
                    print("[SENTRY] Service unhealthy!")

                    incident = Incident(
                        source="Sentry",
                        metrics={"reason": "health_check_failed"}
                    )

                    self.send_event(
                        "Diagnostician",
                        "incident_detected",
                        incident
                    )

                    break

                metrics = requests.get(f"{APP_URL}/metrics").json()

                latency = metrics["latency_ms"]
                error_rate = metrics["error_rate"]

                print(f"[SENTRY] latency={latency} error_rate={error_rate}")

                if latency > 2000 or error_rate > 0.1:
                    print("[SENTRY] anomaly detected!")

                    incident = Incident(
                        source="Sentry",
                        metrics=metrics
                    )

                    print(f"[SENTRY] Incident created → {incident.id}")

                    self.send_event(
                        "Diagnostician",
                        "incident_detected",
                        incident
                    )

                    break

            except Exception as e:
                print("[SENTRY] Service unreachable")

                incident = Incident(
                    source="Sentry",
                    metrics={"reason": "service_down"}
                )

                self.send_event(
                    "Diagnostician",
                    "incident_detected",
                    incident
                )

                break

            time.sleep(5)

    def handle_event(self, event):
        pass
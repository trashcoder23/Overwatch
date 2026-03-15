import requests
import time
from agent_framework.base_agent import BaseAgent
from agent_framework.incident import Incident
import os
APP_URL = os.getenv("APP_URL", "https://demo-service-east.ashyground-9b112b43.eastus.azurecontainerapps.io")


class SentryAgent(BaseAgent):

    def __init__(self, registry):

        super().__init__("Sentry", registry)

    def monitor(self):

        time.sleep(3)

        while True:

            try:

                health = requests.get(f"{APP_URL}/health")

                if health.status_code != 200:

                    print("[SENTRY] Service unhealthy!")

                    incident = Incident(
                        source="Sentry",
                        metrics={"reason": "health_check_failed"}
                    )

                    print(f"[SENTRY] Incident created → {incident.id}")

                    self.send("Diagnostician", "incident_detected", incident)

                metrics = requests.get(f"{APP_URL}/metrics").json()

                latency = metrics["latency_ms"]
                error_rate = metrics["error_rate"]

                print(f"[SENTRY] latency={latency} error_rate={error_rate}")

                if latency > 2000 or error_rate > 0.1:

                    print("[SENTRY] anomaly detected!")

                    incident = Incident(source="Sentry", metrics=metrics)

                    print(f"[SENTRY] Incident created → {incident.id}")

                    self.send("Diagnostician", "incident_detected", incident)

            except Exception:

                print("[SENTRY] Service unreachable")

                incident = Incident(
                    source="Sentry",
                    metrics={"reason": "service_down"}
                )

                self.send("Diagnostician", "incident_detected", incident)

            time.sleep(5)
import requests
import time

APP_URL = "http://127.0.0.1:8000"

class SentryAgent:

    def __init__(self):
        self.health_endpoint = f"{APP_URL}/health"
        self.metrics_endpoint = f"{APP_URL}/metrics"

    def check_health(self):
        try:
            response = requests.get(self.health_endpoint)

            if response.status_code == 200:
                print("[SENTRY] Service healthy")

            else:
                print("[SENTRY] Service unhealthy detected!")
                return "UNHEALTHY"

        except Exception as e:
            print("[SENTRY] Service unreachable!", e)
            return "DOWN"

        return "HEALTHY"

    def check_metrics(self):
        try:
            response = requests.get(self.metrics_endpoint).json()

            latency = response["latency_ms"]
            error_rate = response["error_rate"]

            print(f"[SENTRY] Latency: {latency} ms | Error Rate: {error_rate:.2f}")

            if latency > 2000 or error_rate > 0.1:
                print("[SENTRY] Anomaly detected in metrics")
                return "ANOMALY"

        except Exception as e:
            print("[SENTRY] Metrics fetch failed:", e)

        return "NORMAL"

    def monitor(self):
        while True:
            health = self.check_health()

            if health != "HEALTHY":
                print("[SENTRY] ALERT → Sending incident to Diagnostician")
                break

            metrics = self.check_metrics()

            if metrics == "ANOMALY":
                print("[SENTRY] ALERT → Sending anomaly to Diagnostician")
                break

            time.sleep(5)


if __name__ == "__main__":
    sentry = SentryAgent()
    sentry.monitor()
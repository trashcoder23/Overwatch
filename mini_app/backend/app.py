from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random

app = FastAPI()

# service state simulation
service_state = {
    "status": "healthy"
}

@app.get("/")
def home():
    return {"message": "Overwatch Demo Service Running"}


@app.get("/health")
def health():

    if service_state["status"] == "down":
        return JSONResponse(status_code=500, content={"status": "unhealthy"})

    return {"status": service_state["status"]}


@app.get("/metrics")
def metrics():

    if service_state["status"] == "healthy":

        latency = random.randint(100, 400)
        error_rate = random.uniform(0.0, 0.03)

    elif service_state["status"] == "degraded":

        latency = random.randint(1500, 3000)
        error_rate = random.uniform(0.1, 0.25)

    else:  # down

        latency = random.randint(3000, 5000)
        error_rate = random.uniform(0.3, 0.5)

    return {
        "latency_ms": latency,
        "error_rate": error_rate,
        "service_state": service_state["status"]
    }


# simulate performance degradation
@app.get("/simulate_degradation")
def simulate_degradation():

    service_state["status"] = "degraded"

    return {
        "message": "Service performance degraded"
    }


# simulate full outage
@app.get("/simulate_outage")
def simulate_outage():

    service_state["status"] = "down"

    return {
        "message": "Service outage simulated"
    }


# recover service
@app.get("/recover")
def recover():

    service_state["status"] = "healthy"

    return {
        "message": "Service recovered"
    }
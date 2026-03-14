from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random
import time

app = FastAPI()

# simulate service state
service_status = {
    "healthy": True
}

@app.get("/")
def home():
    return {"message": "Overwatch Demo Service Running"}

@app.get("/health")
def health():
    if service_status["healthy"]:
        return {"status": "healthy"}
    else:
        return JSONResponse(status_code=500, content={"status": "unhealthy"})

@app.get("/simulate_failure")
def simulate_failure():
    service_status["healthy"] = False
    return {"message": "Service failure simulated"}

@app.get("/recover")
def recover():
    service_status["healthy"] = True
    return {"message": "Service recovered"}

@app.get("/metrics")
def metrics():
    return {
        "latency_ms": random.randint(50, 2500),
        "error_rate": random.uniform(0, 0.2)
    }
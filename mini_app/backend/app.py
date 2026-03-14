from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import random
import os

from database import engine
from models import Base
from routes import router


app = FastAPI(
    title="Overwatch Demo Service",
    version="1.0.0"
)

# Database Initialization

@app.on_event("startup")
def startup():

    # create tables if they don't exist
    Base.metadata.create_all(bind=engine)


# Service State

service_state = {
    "status": "healthy"
}

# Root Endpoint (API Info)

@app.get("/api-info")
def api_info():

    return {
        "service": "overwatch-demo",
        "message": "Service running"
    }


# Health Check

@app.get("/health")
def health():

    if service_state["status"] == "down":

        return JSONResponse(
            status_code=500,
            content={"status": "unhealthy"}
        )

    return {
        "status": service_state["status"]
    }


# Metrics Endpoint


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

# Service State Controls
# (Used for testing)


@app.post("/admin/degrade")
def simulate_degradation():

    service_state["status"] = "degraded"

    return {
        "message": "Service performance degraded"
    }


@app.post("/admin/outage")
def simulate_outage():

    service_state["status"] = "down"

    return {
        "message": "Service outage triggered"
    }


@app.post("/admin/recover")
def recover():

    service_state["status"] = "healthy"

    return {
        "message": "Service recovered"
    }

# Include API Routes

app.include_router(router, prefix="/api")

# Serve Frontend


FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "../frontend")

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

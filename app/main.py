from fastapi import FastAPI
from app.routers import events

app = FastAPI(title="SaaS Activity Event Log API", version="1.0.0")
app.include_router(events.router, prefix="/events", tags=["Events"])

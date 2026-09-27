"""
FastAPI application entrypoint.

Run locally with:
    uvicorn app.main:app --reload

Run in production (Render) with:
    uvicorn app.main:app --host 0.0.0.0 --port $PORT
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.database import Base, engine
from app.utils.logger import configure_logging

# Import models package so all ORM models are registered on Base before create_all
import app.models  # noqa: F401

from app.routes import (
    auth,
    predict,
    diseases,
    remedies,
    prevention,
    farming_guide,
    crop_management,
    chat,
    predictions,
    dashboard,
    health,
)

configure_logging()
settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="API for early detection and management of crop diseases and pest infestations",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    # Creates tables if they don't exist. For schema changes in an existing
    # production database, use Alembic migrations (see /alembic) instead.
    Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(predict.router)
app.include_router(diseases.router)
app.include_router(remedies.router)
app.include_router(prevention.router)
app.include_router(farming_guide.router)
app.include_router(crop_management.router)
app.include_router(chat.router)
app.include_router(predictions.router)
app.include_router(dashboard.router)
app.include_router(health.router)


@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running. See /docs for API documentation."}

from fastapi import APIRouter
from sqlalchemy import text

from app.database import SessionLocal
from app.ai.model_loader import model_is_loaded

router = APIRouter(prefix="/api", tags=["health"])


@router.get("/health")
def health_check():
    db_status = "ok"
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
    except Exception as exc:
        db_status = f"error: {exc}"

    return {
        "status": "ok",
        "database": db_status,
        "model_loaded": model_is_loaded(),
    }

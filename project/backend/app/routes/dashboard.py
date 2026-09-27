from collections import Counter

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.prediction import Prediction
from app.models.chat_message import ChatMessage
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/api", tags=["dashboard"])


@router.get("/dashboard")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    predictions = (
        db.query(Prediction).filter(Prediction.user_id == current_user.id).all()
    )
    chat_count = (
        db.query(ChatMessage).filter(ChatMessage.user_id == current_user.id).count()
    )

    class_counts = Counter(p.predicted_class for p in predictions)
    healthy_count = class_counts.get("Healthy", 0)
    disease_count = len(predictions) - healthy_count

    most_recent = max(predictions, key=lambda p: p.created_at, default=None)

    return {
        "total_predictions": len(predictions),
        "healthy_predictions": healthy_count,
        "disease_predictions": disease_count,
        "total_chat_messages": chat_count,
        "predictions_by_class": dict(class_counts),
        "most_recent_prediction": (
            {
                "predicted_class": most_recent.predicted_class,
                "confidence": most_recent.confidence,
                "created_at": most_recent.created_at.isoformat(),
            }
            if most_recent
            else None
        ),
    }

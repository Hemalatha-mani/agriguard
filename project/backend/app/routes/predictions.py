from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.prediction import Prediction
from app.schemas.prediction import PredictionOut
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/api", tags=["predictions"])


@router.get("/predictions", response_model=List[PredictionOut])
def get_prediction_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(Prediction)
        .filter(Prediction.user_id == current_user.id)
        .order_by(Prediction.created_at.desc())
        .all()
    )

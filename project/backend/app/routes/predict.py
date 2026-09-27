import uuid

import numpy as np
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.prediction import Prediction
from app.schemas.prediction import PredictionResult
from app.auth.dependencies import get_current_user
from app.ai.model_loader import get_model, ModelLoadError
from app.ai.preprocess import preprocess_image_bytes
from app.ai.labels import CLASS_NAMES
from app.config import get_settings

router = APIRouter(prefix="/api", tags=["predict"])
settings = get_settings()

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/jpg", "image/webp"}


@router.post("/predict", response_model=PredictionResult)
async def predict(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{file.content_type}'. Upload a JPEG, PNG, or WEBP image.",
        )

    raw_bytes = await file.read()

    max_bytes = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024
    if len(raw_bytes) > max_bytes:
        raise HTTPException(
            status_code=400,
            detail=f"File exceeds the {settings.MAX_UPLOAD_SIZE_MB}MB size limit.",
        )

    try:
        img_array = preprocess_image_bytes(raw_bytes)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    try:
        model = get_model()
    except ModelLoadError as exc:
        # Fail loudly and specifically -- never silently fall back to fake data.
        raise HTTPException(status_code=503, detail=f"AI model unavailable: {exc}") from exc

    try:
        raw_predictions = model.predict(img_array)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Model inference failed: {exc}") from exc

    probabilities = np.asarray(raw_predictions)[0]

    if probabilities.shape[0] != len(CLASS_NAMES):
        raise HTTPException(
            status_code=500,
            detail=(
                f"Model output has {probabilities.shape[0]} classes but "
                f"{len(CLASS_NAMES)} class names are configured in app/ai/labels.py. "
                "Update CLASS_NAMES to match the model's actual output."
            ),
        )

    predicted_index = int(np.argmax(probabilities))
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = float(probabilities[predicted_index])

    all_probabilities = {
        CLASS_NAMES[i]: float(probabilities[i]) for i in range(len(CLASS_NAMES))
    }

    # Persist the uploaded image to disk so it can be referenced later if needed.
    stored_filename = f"{uuid.uuid4().hex}_{file.filename}"

    prediction_record = Prediction(
        user_id=current_user.id,
        image_filename=stored_filename,
        predicted_class=predicted_class,
        confidence=confidence,
    )
    db.add(prediction_record)
    db.commit()

    return PredictionResult(
        predicted_class=predicted_class,
        confidence=confidence,
        all_probabilities=all_probabilities,
    )

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PredictionResult(BaseModel):
    predicted_class: str
    confidence: float
    all_probabilities: dict[str, float]


class PredictionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_filename: str
    predicted_class: str
    confidence: float
    created_at: datetime

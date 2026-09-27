from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas.disease import Remedy
from app.data.remedies_data import REMEDIES, REMEDIES_BY_DISEASE_ID

router = APIRouter(prefix="/api/remedies", tags=["remedies"])


@router.get("", response_model=List[Remedy])
def list_remedies():
    return REMEDIES


@router.get("/{disease_id}", response_model=Remedy)
def get_remedy(disease_id: str):
    remedy = REMEDIES_BY_DISEASE_ID.get(disease_id)
    if not remedy:
        raise HTTPException(status_code=404, detail="Remedy not found for this disease")
    return remedy

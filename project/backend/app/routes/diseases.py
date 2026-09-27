from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.schemas.disease import Disease
from app.data.diseases_data import DISEASES, DISEASES_BY_ID

router = APIRouter(prefix="/api/diseases", tags=["diseases"])


@router.get("", response_model=List[Disease])
def list_diseases(
    crop: Optional[str] = Query(None, description="Filter by crop name, e.g. Potato"),
    search: Optional[str] = Query(None, description="Search by disease name"),
):
    results = DISEASES

    if crop:
        results = [d for d in results if d["crop"].lower() == crop.lower()]

    if search:
        term = search.lower()
        results = [d for d in results if term in d["name"].lower()]

    return results


@router.get("/{disease_id}", response_model=Disease)
def get_disease(disease_id: str):
    disease = DISEASES_BY_ID.get(disease_id)
    if not disease:
        raise HTTPException(status_code=404, detail="Disease not found")
    return disease

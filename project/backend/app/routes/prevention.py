from typing import List

from fastapi import APIRouter

from app.schemas.disease import PreventionTip
from app.data.prevention_data import PREVENTION_TIPS

router = APIRouter(prefix="/api/prevention", tags=["prevention"])


@router.get("", response_model=List[PreventionTip])
def get_prevention_tips():
    return PREVENTION_TIPS

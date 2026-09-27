from typing import List

from fastapi import APIRouter

from app.schemas.disease import FarmingGuideEntry
from app.data.farming_guide_data import FARMING_GUIDE

router = APIRouter(prefix="/api/farming-guide", tags=["farming-guide"])


@router.get("", response_model=List[FarmingGuideEntry])
def get_farming_guide():
    return FARMING_GUIDE

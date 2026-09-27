from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas.disease import CropManagementEntry
from app.data.crop_management_data import CROP_MANAGEMENT, CROP_MANAGEMENT_BY_NAME

router = APIRouter(prefix="/api/crop-management", tags=["crop-management"])


@router.get("", response_model=List[CropManagementEntry])
def list_crop_management():
    return CROP_MANAGEMENT


@router.get("/{crop_name}", response_model=CropManagementEntry)
def get_crop_management(crop_name: str):
    entry = CROP_MANAGEMENT_BY_NAME.get(crop_name.lower())
    if not entry:
        raise HTTPException(status_code=404, detail="Crop not found")
    return entry

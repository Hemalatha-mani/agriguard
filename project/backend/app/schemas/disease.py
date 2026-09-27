from typing import List
from pydantic import BaseModel


class Disease(BaseModel):
    id: str
    name: str
    crop: str
    image: str
    severity: str
    symptoms: List[str]
    causes: List[str]
    identification_signs: List[str]
    detailed_info: str


class Remedy(BaseModel):
    disease_id: str
    disease_name: str
    crop: str
    immediate_actions: List[str]
    natural_management: List[str]
    cultural_management: List[str]
    treatment_category: str
    safety_information: str
    when_to_seek_expert_help: str


class PreventionTip(BaseModel):
    crop: str
    title: str
    points: List[str]


class FarmingGuideEntry(BaseModel):
    title: str
    stage: str
    content: List[str]


class CropManagementEntry(BaseModel):
    crop_name: str
    ideal_conditions: str
    watering: str
    fertilization: str
    common_pests: List[str]
    harvesting_tips: str

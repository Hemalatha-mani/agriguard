"""
Structured reference data for the 5 disease classes the model can detect
(plus the Healthy class is excluded here since it is not a disease).

This is reference/educational content, kept separate from route logic so
it can be edited or later migrated into the database without touching
any endpoint code.
"""

DISEASES = [
    {
        "id": "potato_early_blight",
        "name": "Potato Early Blight",
        "crop": "Potato",
        "image": "/images/diseases/potato_early_blight.jpg",
        "severity": "Moderate",
        "symptoms": [
            "Dark brown to black concentric ring spots on older leaves",
            "Yellowing of tissue surrounding the spots",
            "Lesions enlarging and merging as disease progresses",
            "Premature leaf drop starting from the lower canopy",
        ],
        "causes": [
            "Fungal pathogen Alternaria solani",
            "Warm, humid weather (24-29°C) with periods of leaf wetness",
            "Nutrient-stressed or aging plants",
        ],
        "identification_signs": [
            "Target-like concentric rings inside lesions",
            "Spots typically appear on lower/older leaves first",
        ],
        "detailed_info": (
            "Early blight is one of the most common potato foliar diseases, caused by "
            "the fungus Alternaria solani. It thrives in warm, humid conditions and "
            "spreads through wind, rain splash, and infected plant debris. Left "
            "untreated it can significantly reduce yield by causing early defoliation."
        ),
    },
    {
        "id": "potato_late_blight",
        "name": "Potato Late Blight",
        "crop": "Potato",
        "image": "/images/diseases/potato_late_blight.jpg",
        "severity": "Severe",
        "symptoms": [
            "Water-soaked pale to dark green lesions on leaves",
            "White fungal growth on the underside of leaves in humid conditions",
            "Rapid blackening and collapse of foliage",
            "Brown rot on tubers with a granular texture",
        ],
        "causes": [
            "Oomycete pathogen Phytophthora infestans",
            "Cool, wet weather with high humidity",
            "Infected seed tubers or nearby infected plants",
        ],
        "identification_signs": [
            "Rapidly expanding, irregularly shaped water-soaked lesions",
            "White mold ring visible at the edge of lesions on leaf undersides",
        ],
        "detailed_info": (
            "Late blight is a highly destructive disease historically responsible for "
            "the Irish potato famine. It spreads extremely quickly under cool, moist "
            "conditions and can destroy an entire field within days if not managed."
        ),
    },
    {
        "id": "tomato_bacterial_spot",
        "name": "Tomato Bacterial Spot",
        "crop": "Tomato",
        "image": "/images/diseases/tomato_bacterial_spot.jpg",
        "severity": "Moderate",
        "symptoms": [
            "Small, water-soaked spots on leaves that turn dark brown",
            "Spots with yellow halos on leaves",
            "Raised, scab-like spots on fruit",
        ],
        "causes": [
            "Bacterial pathogens of the genus Xanthomonas",
            "Warm, wet, and humid weather",
            "Spread via splashing water, contaminated tools, and infected seed",
        ],
        "identification_signs": [
            "Angular leaf spots that may fall out, giving a 'shot-hole' look",
            "Scabby raised lesions on green fruit",
        ],
        "detailed_info": (
            "Bacterial spot affects tomato leaves, stems, and fruit, reducing "
            "marketable yield. Unlike fungal diseases, it cannot be controlled with "
            "standard fungicides, so cultural and copper-based bactericide practices "
            "are the primary defense."
        ),
    },
    {
        "id": "tomato_early_blight",
        "name": "Tomato Early Blight",
        "crop": "Tomato",
        "image": "/images/diseases/tomato_early_blight.jpg",
        "severity": "Moderate",
        "symptoms": [
            "Concentric-ring 'bullseye' spots on lower leaves",
            "Yellowing around lesions",
            "Stem lesions near the soil line",
            "Dark, sunken spots on fruit near the stem",
        ],
        "causes": [
            "Fungal pathogen Alternaria solani (also affects potato)",
            "Warm temperatures with alternating wet and dry periods",
            "Splash dispersal from soil-borne spores",
        ],
        "identification_signs": [
            "Target-like concentric rings, similar to potato early blight",
            "Progresses from oldest to youngest leaves",
        ],
        "detailed_info": (
            "Tomato early blight is caused by the same fungal genus as potato early "
            "blight and shares similar symptoms and management strategies. It is "
            "favored by crowded plantings and poor air circulation."
        ),
    },
    {
        "id": "tomato_late_blight",
        "name": "Tomato Late Blight",
        "crop": "Tomato",
        "image": "/images/diseases/tomato_late_blight.jpg",
        "severity": "Severe",
        "symptoms": [
            "Large, irregular greasy-looking lesions on leaves",
            "White fuzzy mold on leaf undersides in humid weather",
            "Firm, dark, greasy-looking blotches on fruit",
            "Rapid whole-plant collapse",
        ],
        "causes": [
            "Oomycete pathogen Phytophthora infestans",
            "Cool, wet, humid conditions",
            "Wind-blown spores from nearby infected potato or tomato plants",
        ],
        "identification_signs": [
            "Lesions expand within 24-48 hours in favorable conditions",
            "Distinct musty odor from severely infected plants",
        ],
        "detailed_info": (
            "Tomato late blight is one of the most feared tomato diseases due to its "
            "speed of spread and ability to destroy a crop in days. Immediate action "
            "is critical once symptoms are spotted."
        ),
    },
]

DISEASES_BY_ID = {d["id"]: d for d in DISEASES}

# Maps a raw model class name (as in app.ai.labels.CLASS_NAMES) to the
# disease id used throughout this data module and the API.
MODEL_CLASS_TO_DISEASE_ID = {
    "Healthy": None,
    "Potato_Early_blight": "potato_early_blight",
    "Potato_Late_blight": "potato_late_blight",
    "Tomato_Bacterial_spot": "tomato_bacterial_spot",
    "Tomato_Early_blight": "tomato_early_blight",
    "Tomato_Late_blight": "tomato_late_blight",
}

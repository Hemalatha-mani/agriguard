"""Structured per-crop management data."""

CROP_MANAGEMENT = [
    {
        "crop_name": "Potato",
        "ideal_conditions": "Cool climate, 15-20°C, well-drained loamy soil, pH 5.0-6.5",
        "watering": "1-2 inches per week; consistent moisture during tuber formation",
        "fertilization": "Balanced NPK at planting; supplement with potassium during tuber bulking",
        "common_pests": ["Colorado potato beetle", "Aphids", "Wireworms"],
        "harvesting_tips": "Harvest after foliage dies back; cure tubers in a cool, dark, ventilated space",
    },
    {
        "crop_name": "Tomato",
        "ideal_conditions": "Warm climate, 20-27°C, well-drained fertile soil, pH 6.0-6.8",
        "watering": "Deep watering 1-2 times per week at the base; avoid wetting foliage",
        "fertilization": "Balanced fertilizer at planting, then higher phosphorus/potassium during fruiting",
        "common_pests": ["Whiteflies", "Aphids", "Hornworms", "Spider mites"],
        "harvesting_tips": "Pick fruit when fully colored but still firm; harvest regularly to encourage yield",
    },
]

CROP_MANAGEMENT_BY_NAME = {c["crop_name"].lower(): c for c in CROP_MANAGEMENT}

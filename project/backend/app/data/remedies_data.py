"""Structured remedy data, one entry per disease id (see diseases_data.py)."""

REMEDIES = [
    {
        "disease_id": "potato_early_blight",
        "disease_name": "Potato Early Blight",
        "crop": "Potato",
        "immediate_actions": [
            "Remove and destroy severely infected leaves",
            "Avoid overhead irrigation to reduce leaf wetness",
            "Apply a labeled fungicide (e.g. chlorothalonil or copper-based) per product instructions",
        ],
        "natural_management": [
            "Neem oil spray on affected foliage",
            "Compost tea as a soil health / foliar treatment",
            "Baking soda solution (mild antifungal effect) for early-stage infections",
        ],
        "cultural_management": [
            "Rotate crops with non-solanaceous plants for 2-3 years",
            "Space plants to improve air circulation",
            "Mulch to prevent soil splash onto lower leaves",
            "Remove plant debris at end of season",
        ],
        "treatment_category": "Fungal",
        "safety_information": (
            "Always follow label instructions on any fungicide. Wear gloves and a mask "
            "when spraying, and observe the pre-harvest interval before eating produce."
        ),
        "when_to_seek_expert_help": (
            "If more than 30% of the plant canopy is affected or the disease spreads "
            "rapidly despite treatment, consult a local agricultural extension officer."
        ),
    },
    {
        "disease_id": "potato_late_blight",
        "disease_name": "Potato Late Blight",
        "crop": "Potato",
        "immediate_actions": [
            "Remove and destroy (do not compost) infected plants immediately",
            "Apply a systemic or protectant fungicide labeled for late blight promptly",
            "Improve field drainage to reduce humidity around plants",
        ],
        "natural_management": [
            "Copper-based organic fungicides applied preventatively",
            "Ensure wide plant spacing to reduce microclimate humidity",
        ],
        "cultural_management": [
            "Use certified disease-free seed potatoes",
            "Avoid planting near infected potato or tomato fields",
            "Hill soil around stems to protect tubers from spores washing down",
        ],
        "treatment_category": "Oomycete (fungus-like)",
        "safety_information": (
            "Late blight spreads extremely fast — treat as an emergency. Follow all "
            "fungicide label safety precautions and re-entry intervals."
        ),
        "when_to_seek_expert_help": (
            "Late blight can destroy a field within days. Contact an agricultural "
            "extension service immediately upon suspicion, even before lab confirmation."
        ),
    },
    {
        "disease_id": "tomato_bacterial_spot",
        "disease_name": "Tomato Bacterial Spot",
        "crop": "Tomato",
        "immediate_actions": [
            "Remove and destroy infected leaves and fruit",
            "Apply copper-based bactericide (fungicides are not effective on bacteria)",
            "Avoid working in the field when foliage is wet",
        ],
        "natural_management": [
            "Copper + mancozeb combination sprays where locally approved",
            "Compost tea to support overall plant immunity",
        ],
        "cultural_management": [
            "Use pathogen-free certified seed and transplants",
            "Practice 2-3 year crop rotation",
            "Avoid overhead watering; use drip irrigation instead",
            "Disinfect tools between plants",
        ],
        "treatment_category": "Bacterial",
        "safety_information": (
            "Copper products can build up in soil with repeated use — follow "
            "recommended application rates and intervals."
        ),
        "when_to_seek_expert_help": (
            "If bacterial spot recurs across seasons despite rotation and sanitation, "
            "seek expert help to test soil and seed sources."
        ),
    },
    {
        "disease_id": "tomato_early_blight",
        "disease_name": "Tomato Early Blight",
        "crop": "Tomato",
        "immediate_actions": [
            "Prune and destroy lower infected leaves",
            "Apply a labeled fungicide (chlorothalonil, copper, or azoxystrobin)",
            "Stake plants to keep foliage off the ground",
        ],
        "natural_management": [
            "Neem oil or copper soap sprays",
            "Baking soda + horticultural oil spray for mild cases",
        ],
        "cultural_management": [
            "Mulch around base to prevent soil splash",
            "Rotate with non-solanaceous crops",
            "Water at the base of plants, not the foliage",
        ],
        "treatment_category": "Fungal",
        "safety_information": (
            "Follow fungicide label directions exactly, including pre-harvest intervals."
        ),
        "when_to_seek_expert_help": (
            "If defoliation progresses rapidly up the plant despite treatment, "
            "consult a local extension service."
        ),
    },
    {
        "disease_id": "tomato_late_blight",
        "disease_name": "Tomato Late Blight",
        "crop": "Tomato",
        "immediate_actions": [
            "Remove and destroy infected plants immediately, do not compost",
            "Apply a protectant fungicide to remaining healthy plants right away",
            "Increase spacing/airflow around remaining plants",
        ],
        "natural_management": [
            "Preventative copper-based sprays before symptoms appear in high-risk weather",
        ],
        "cultural_management": [
            "Avoid planting tomatoes near potatoes",
            "Choose resistant tomato varieties where available",
            "Water early in the day so foliage dries before evening",
        ],
        "treatment_category": "Oomycete (fungus-like)",
        "safety_information": (
            "Treat as an emergency — late blight can spread across a field in days."
        ),
        "when_to_seek_expert_help": (
            "Contact an agricultural extension service immediately upon suspicion."
        ),
    },
]

REMEDIES_BY_DISEASE_ID = {r["disease_id"]: r for r in REMEDIES}

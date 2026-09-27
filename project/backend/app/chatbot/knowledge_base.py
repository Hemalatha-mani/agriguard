"""
Knowledge base for the rule-based agricultural chatbot.

Each entry has a list of trigger keywords and a response. The engine
scores each entry by how many of its keywords appear in the user's
message and returns the best match. This is a genuine (if simple)
retrieval mechanism — not a hardcoded canned reply to every question.

To upgrade this to an LLM-backed chatbot later, swap engine.get_answer()
to call an external API while keeping this file as a fallback / grounding
knowledge source.
"""

KNOWLEDGE_BASE = [
    {
        "keywords": ["early blight", "alternaria"],
        "answer": (
            "Early blight (caused by Alternaria solani) affects potatoes and tomatoes. "
            "Look for dark, concentric 'target-ring' spots on older leaves. Manage it by "
            "removing infected leaves, rotating crops, improving air circulation, and "
            "applying a labeled fungicide such as chlorothalonil or a copper-based product."
        ),
    },
    {
        "keywords": ["late blight", "phytophthora"],
        "answer": (
            "Late blight (Phytophthora infestans) is a fast-spreading, serious disease of "
            "potato and tomato. Watch for water-soaked lesions that turn brown/black with "
            "white fungal growth on leaf undersides in humid weather. Act immediately: "
            "remove infected plants, apply a protectant fungicide, and improve spacing "
            "and airflow. It can destroy a field within days."
        ),
    },
    {
        "keywords": ["bacterial spot", "xanthomonas"],
        "answer": (
            "Bacterial spot causes small, water-soaked, dark leaf spots with yellow halos "
            "and scabby lesions on fruit. Fungicides won't help since it's bacterial — use "
            "copper-based bactericides, disease-free seed, drip irrigation instead of "
            "overhead watering, and crop rotation."
        ),
    },
    {
        "keywords": ["watering", "irrigation", "water"],
        "answer": (
            "For disease prevention, water at the base of plants rather than overhead — "
            "wet foliage encourages fungal and bacterial diseases. Water deeply but less "
            "frequently to encourage strong root growth, and water early in the day so "
            "leaves dry before nightfall."
        ),
    },
    {
        "keywords": ["prevent", "prevention", "avoid disease"],
        "answer": (
            "Key prevention practices: rotate crops every 2-3 years, use certified "
            "disease-free seed, space plants for good airflow, avoid overhead watering, "
            "remove crop debris after harvest, and scout your fields weekly so you catch "
            "problems early."
        ),
    },
    {
        "keywords": ["crop management", "manage crop", "manage my crop"],
        "answer": (
            "Good crop management combines the right planting density, balanced "
            "fertilization based on soil tests, consistent irrigation, regular pest and "
            "disease scouting, and timely harvesting. Check the Crop Management page for "
            "crop-specific guidance."
        ),
    },
    {
        "keywords": ["farming", "farm", "agriculture tips"],
        "answer": (
            "Successful farming starts with soil preparation and testing, choosing "
            "resistant varieties suited to your region, proper spacing, balanced "
            "nutrition, and consistent monitoring throughout the growing season. See the "
            "Farming Guide page for a full stage-by-stage walkthrough."
        ),
    },
    {
        "keywords": ["potato"],
        "answer": (
            "Potatoes prefer cool climates (15-20°C) and well-drained loamy soil "
            "(pH 5.0-6.5). Watch particularly for early blight and late blight, both of "
            "which are common and can significantly reduce yield if untreated."
        ),
    },
    {
        "keywords": ["tomato"],
        "answer": (
            "Tomatoes prefer warm climates (20-27°C) and fertile, well-drained soil "
            "(pH 6.0-6.8). Watch for early blight, late blight, and bacterial spot — all "
            "three affect tomato foliage and fruit."
        ),
    },
    {
        "keywords": ["healthy", "is my plant healthy", "disease free"],
        "answer": (
            "Healthy plants show uniform green leaf color, no spotting or lesions, and "
            "steady growth. If you're unsure, upload a photo on the AI Detect page for an "
            "instant assessment based on our trained model."
        ),
    },
]

FALLBACK_ANSWER = (
    "I can help with questions about crops, plant diseases, prevention, watering, "
    "farming practices, and crop management — including early blight, late blight, and "
    "bacterial spot. Could you rephrase your question, or try the AI Detect page if you "
    "have a photo of an affected plant?"
)

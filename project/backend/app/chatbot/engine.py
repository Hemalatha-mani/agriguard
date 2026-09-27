"""
Rule-based chatbot engine.

This chatbot answers general agricultural text questions. It never claims
to have performed image-based diagnosis — for that, users must use the
AI Detect page which calls the real Keras model.
"""
import re

from app.chatbot.knowledge_base import KNOWLEDGE_BASE, FALLBACK_ANSWER

_DIAGNOSIS_PHRASES = ["diagnose my plant", "what disease is this", "look at my plant"]


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9\s]", " ", text.lower())


def get_answer(user_message: str) -> str:
    normalized = _normalize(user_message)

    # If the user seems to be asking for an image diagnosis via chat text,
    # redirect them to the AI Detect page instead of pretending to analyze anything.
    if any(phrase in normalized for phrase in _DIAGNOSIS_PHRASES):
        return (
            "I can't diagnose a plant from a text description alone. Please go to the "
            "AI Detect page and upload a clear photo of the affected leaf — our trained "
            "model will analyze the actual image."
        )

    best_entry = None
    best_score = 0

    for entry in KNOWLEDGE_BASE:
        score = sum(1 for kw in entry["keywords"] if kw in normalized)
        if score > best_score:
            best_score = score
            best_entry = entry

    if best_entry is not None and best_score > 0:
        return best_entry["answer"]

    return FALLBACK_ANSWER

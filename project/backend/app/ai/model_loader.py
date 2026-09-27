"""
Lazy loader for the trained crop disease detection model.

The model is NOT loaded at import time or app startup. It is loaded once,
on the first prediction request, and cached in-process afterward. This
keeps API startup fast and avoids loading TensorFlow at all for routes
that never touch the model.

There is no dummy/fake model fallback: if the real .keras file is missing
or fails to load, /api/predict must fail loudly with a clear error so the
problem gets fixed rather than hidden.
"""
import logging
import os
import threading
from typing import Optional

from app.config import get_settings

logger = logging.getLogger("model_loader")

_model = None
_model_lock = threading.Lock()


class ModelLoadError(RuntimeError):
    """Raised when the real Keras model cannot be loaded."""


def get_model():
    """
    Returns the cached Keras model, loading it on first call.
    Thread-safe via a lock so concurrent requests don't trigger duplicate loads.
    """
    global _model

    if _model is not None:
        return _model

    with _model_lock:
        if _model is not None:  # re-check after acquiring the lock
            return _model

        settings = get_settings()
        model_path = settings.MODEL_PATH

        if not os.path.isfile(model_path):
            raise ModelLoadError(
                f"Model file not found at '{model_path}'. Place "
                "crop_disease_model_final.keras at that path (relative to the "
                "backend working directory) or set MODEL_PATH in the environment."
            )

        try:
            # Imported here (not at module load time) so TensorFlow is only
            # pulled into memory when a prediction actually happens.
            import tensorflow as tf
        except Exception as exc:
            raise ModelLoadError(
                f"Failed to import TensorFlow: {exc}. Check that the "
                "tensorflow version in requirements.txt matches your Python "
                "version and platform."
            ) from exc

        try:
            logger.info("Loading model from %s ...", model_path)
            _model = tf.keras.models.load_model(model_path)
            logger.info("Model loaded successfully.")
        except Exception as exc:
            raise ModelLoadError(
                f"Failed to load Keras model from '{model_path}': {exc}"
            ) from exc

    return _model


def model_is_loaded() -> bool:
    return _model is not None

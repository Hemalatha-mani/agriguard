"""
Image preprocessing for crop_disease_model_final.keras.

Model input spec: 224x224x3, float32, pixel values scaled to [0, 1].
If your model was trained with a different preprocessing function
(e.g. tf.keras.applications.mobilenet_v2.preprocess_input, which scales to
[-1, 1]), update `normalize()` to match exactly — a mismatch here will
silently produce wrong predictions even though the code runs without error.
"""
import io

import numpy as np
from PIL import Image

from app.config import get_settings

settings = get_settings()


def normalize(img_array: np.ndarray) -> np.ndarray:
    return img_array.astype("float32") / 255.0


def preprocess_image_bytes(image_bytes: bytes) -> np.ndarray:
    """
    Converts raw uploaded image bytes into a (1, 224, 224, 3) float32 array
    ready to feed into model.predict().
    """
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    except Exception as exc:
        raise ValueError(f"Uploaded file is not a valid image: {exc}") from exc

    size = settings.MODEL_INPUT_SIZE
    image = image.resize((size, size))

    img_array = np.array(image)
    img_array = normalize(img_array)
    img_array = np.expand_dims(img_array, axis=0)  # batch dimension

    return img_array

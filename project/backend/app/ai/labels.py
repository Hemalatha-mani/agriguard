"""
Class labels for crop_disease_model_final.keras.

IMPORTANT: This order must exactly match the order the model was trained
with (i.e. the order Keras's ImageDataGenerator / image_dataset_from_directory
assigned during training — normally alphabetical by folder name). If your
training pipeline used a different order, update this list to match, or the
predicted index will map to the wrong class name.
"""

CLASS_NAMES = [
    "Healthy",
    "Potato_Early_blight",
    "Potato_Late_blight",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
]

NUM_CLASSES = len(CLASS_NAMES)

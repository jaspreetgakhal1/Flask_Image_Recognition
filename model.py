"""Utilities for loading the trained digit-recognition model and preprocessing images."""

from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image

# Loading model
model = load_model("digit_model.h5")


def preprocess_img(img_path):
    """Open an image, resize it, and prepare it for model inference."""
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    img2arr = img_to_array(img_resize) / 255.0
    img_reshape = img2arr.reshape(1, 224, 224, 3)
    return img_reshape


def predict_result(processed_image):
    """Return the predicted digit class for a processed image."""
    prediction = model.predict(processed_image)
    return int(np.argmax(prediction[0], axis=-1))

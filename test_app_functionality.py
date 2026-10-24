"""Focused tests for the Flask app and image preprocessing pipeline."""

from io import BytesIO

import numpy as np

import app as app_module
from model import preprocess_img


def test_home_page_accessible(client):
    """The main page should load successfully."""
    response = client.get("/")

    assert response.status_code == 200
    assert b"Hand Sign Digit Language Detection" in response.data


def test_valid_upload_returns_prediction(client):
    """A valid uploaded image should produce a prediction page."""
    with open("test_images/0/Sign 0 (116).jpeg", "rb") as image_file:
        response = client.post(
            "/prediction",
            data={"file": (image_file, "Sign 0 (116).jpeg")},
            content_type="multipart/form-data",
        )

    assert response.status_code == 200
    assert b"Prediction" in response.data


def test_missing_file_is_handled(client):
    """A request without an uploaded file should show an error message."""
    response = client.post(
        "/prediction",
        data={},
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data


def test_invalid_input_is_handled(client, monkeypatch):
    """Unexpected processing errors should return a friendly message."""
    def raise_value_error(_):
        raise ValueError("bad image")

    monkeypatch.setattr(app_module, "preprocess_img", raise_value_error)

    response = client.post(
        "/prediction",
        data={"file": (BytesIO(b"not-a-real-image"), "broken.jpg")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    assert b"File cannot be processed." in response.data


def test_preprocess_img_resizes_and_normalizes_image():
    """The preprocessing function should reshape image data to model input size."""
    processed = preprocess_img("test_images/2/Sign 2 (97).jpeg")

    assert processed.shape == (1, 224, 224, 3)
    assert np.min(processed) >= 0
    assert np.max(processed) <= 1

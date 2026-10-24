"""Flask application for handwritten digit image recognition."""

from flask import Flask, render_template, request

from model import preprocess_img, predict_result

# Instantiating flask app
app = Flask(__name__)


@app.route("/")
def main():
    """Render the upload page."""
    return render_template("index.html")


@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """Accept an uploaded image, predict its digit, and render the result."""
    if request.method != 'POST':
        return render_template("result.html", err="File cannot be processed.")

    uploaded_file = request.files.get('file')
    if uploaded_file is None or uploaded_file.filename == '':
        return render_template("result.html", err="File cannot be processed.")

    try:
        img = preprocess_img(uploaded_file.stream)
        pred = predict_result(img)
    except (TypeError, ValueError, OSError):
        return render_template("result.html", err="File cannot be processed.")

    return render_template("result.html", predictions=str(pred))


if __name__ == "__main__":
    app.run(port=9000, debug=True)

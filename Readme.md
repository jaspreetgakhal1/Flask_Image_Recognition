# Hand Digit Image Recognition

This web app is made using Flask framework and is all about predicting the hand sign digit images based on the deep learning model trained using transfer learning.

![Python](https://img.shields.io/badge/python-8338ec)
![Keras](https://img.shields.io/badge/keras-219ebc)
![Numpy](https://img.shields.io/badge/numpy-ffafcc)
![Pillow](https://img.shields.io/badge/pillow-00bbf9)
![Flask](https://img.shields.io/badge/flask-f72585)
![Bootstrap](https://img.shields.io/badge/bootstrap-57cc99)

# Glimpse

https://user-images.githubusercontent.com/72191416/201943098-c8f5fd8b-ec7d-4e5d-883d-8b69109b946f.mp4

# Dependencies

- Flask
- TensorFlow (Keras)
- Numpy
- Pillow (PIL)

## UI Framework

- Bootstrap

# Get Started

Clone the repository in your project directory.

```commandline
git clone https://github.com/Sachin-crypto/Flask_Image_Recognition.git
```
OR

Download as **[ZIP](https://github.com/Sachin-crypto/Flask_Image_Recognition/archive/refs/heads/main.zip)** file and extract it in your project directory.

# Install Dependencies

Create a local virtual environment and install the project dependencies from the **requirements.txt** file.

```commandline
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Compatibility note

The original project pinned TensorFlow 2.10, which is not compatible with the Python 3.9 runtime used in this environment. The dependency set was updated to a compatible stack (`tensorflow==2.15.1`, `keras==2.15.0`, `Werkzeug==2.3.3`) so the app runs successfully on modern macOS systems.

# Run

**cd** into the current directory and run the script.

```commandline
flask --app app.py run --host 0.0.0.0 --port 9000
```

Click [here](https://geekpython.in/run-flask-app-from-the-command-line-in-windows) to get the detailed guide on running the Flask app from the command line.

# Code Quality Checks

Install the development tools used for linting and pre-commit checks.

```commandline
python -m pip install -r requirements-dev.txt
pre-commit install
```

Run the checks manually when needed:

```commandline
python -m pylint app.py model.py
python -m pytest -q
pre-commit run --all-files
```

# CI progression during development

This was not something I added only at the end. The project went through a few steps while I was making it work properly and setting up CI in a realistic way.

- The first GitHub Actions workflow was added early in the project.
- I then updated the dependency and test setup so the workflow could run correctly with the project environment.
- After that, I added linting and quality tools so the code would be checked before the final version was considered ready.
- I also added pre-commit checks so formatting and simple issues were caught before code was pushed.
- The workflow was then finalized to run automatically on push and pull request.

This was useful because the checks actually caught problems during development:

- Pylint picked up quality issues in the older Flask code and model file. I fixed those issues and then reran the lint check.
- Pytest caught problems in the app behavior and edge cases during the acceptance and integration testing work. Those fixes were tested again before moving on.
- Pre-commit found formatting and whitespace issues early, which made it easier to keep the repo clean.

So the project shows a real development process: setup, fixing issues, adding checks, and making sure the project stays stable as it improves.

# Test

```commandline
python -m pytest -q
```

- Choose an image from the test images folder.
- You will see a preview of the uploaded image.
- Click on **Submit** button and see the magic.

### Rasa Chatbot Project

# Rasa Environment Setup Guide

https://rasa.com/docs/rasa/installation/environment-set-up/

# Flask Setup Guide

## Step 1: Install Python

1. Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for Windows.
2. Once the download is complete, run the installer and follow the instructions to install Python on your system.
3. During the installation process, make sure to select the option to **Add Python to PATH**.

## Step 2: Install VS Code

1. Visit the [official VS Code website](https://code.visualstudio.com/) and download the latest version of VS Code for Windows.
2. Once the download is complete, run the installer and follow the instructions to install VS Code on your system.

## Step 3: Create a Virtual Environment

1. Open a new terminal window in VS Code.
2. Navigate to the root directory of your project.
3. Run the following command to create a new virtual environment:

    ```bash
    python -m venv venv
    ```

This command creates a virtual environment named `venv` in the root directory of your project.

## Step 4: Activate the Virtual Environment

To activate the virtual environment, run the following command in the terminal:

    ```bash
    venv\Scripts\activate
    ```

## Step 5: Install Flask

With the virtual environment activated, we can now install Flask using pip, the package manager for Python.

1. Open your terminal.
2. Run the following command to install Flask:

    ```bash
    pip install flask
    ```

This command will download and install Flask and all its dependencies in your virtual environment.

## Step 6: Create a Flask Application

Now that Flask is installed, and the application is already created, run the application.

OR, you can create a new Flask application:

1. In the root directory of your project, create a new Python file named `app.py`.
2. Add the following code to `app.py`:

    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, World!'
    ```

This code creates a new Flask application with a single route that returns the string `Hello, World!` when the root URL is accessed.

## Step 7: Run the Flask Application

With the Flask application created, you can now run it using the following command:

    ```bash
    flask run
    ```

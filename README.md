# Flask Heroku Deployment

This project demonstrates how to deploy a simple Flask application to Heroku. The following instructions will guide you through setting up the project, deploying it to Heroku, and running it locally.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/download/win)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/sentiment-analysis.git
    cd sentiment-analysis
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

1. **Set environment variables** (if needed):
    ```bash
    set FLASK_APP=app.py
    set FLASK_ENV=development
    ```

2. **Run the Flask app**:
    ```bash
    flask run
    ```

3. **Access the app**:
    Open your browser and navigate to `http://localhost:5000`.

## Deploying to Heroku

1. **Login to Heroku**:
    ```bash
    heroku login
    ```

2. **Create a new Heroku app**:
    ```bash
    heroku create
    ```

3. **Add the Heroku remote**:
    ```bash
    git remote add heroku https://git.heroku.com/your-app-name.git
    ```

4. **Deploy the app**:
    ```bash
    git add .
    git commit -m "Initial commit"
    git push heroku master
    ```

5. **Open the app in your browser**:
    ```bash
    heroku open
    ```

## File Structure
sentiment-analysis/
│
├── app.py
├── requirements.txt
├── Procfile
└── README.md

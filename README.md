# Processor Recommendation API - Flask Backend

[![Python][Python-shield]][Python-url]
[![Flask][Flask-shield]][Flask-url]
[![Scikit-learn][Scikit-learn-shield]][Scikit-learn-url]
[![Render][Render-shield]][Render-url]

### 🚀 [View the Live API Base URL](https://processor-recom-api.onrender.com/) 🚀
*(Note: The root URL shows a legacy HTML page. The API endpoints are at `/api/...`)*

---

## About The Project

This is a Python-based REST API built with Flask to serve predictions from a custom-trained machine learning model. It acts as the "brain" for the [Processor Analysis Engine React Frontend](https://github.com/MdEhsanulHaqueKanan/processor-analysis-frontend).

The API is responsible for:
1.  Loading a dataset of processor specifications.
2.  Filtering the dataset based on criteria sent from the frontend.
3.  Loading trained Scikit-learn models (`.joblib` files).
4.  Serving predictions from the models via JSON-based API endpoints.

## API Endpoints

*   `POST /api/recommend`
    *   Accepts a JSON object with filter criteria (`designer`, `min_year`, `max_cores`, etc.).
    *   Returns a JSON array of processor objects that match the criteria.

*   `POST /api/predict`
    *   Accepts a JSON object with custom processor specifications.
    *   Returns a JSON object with the model's predictions for the processor's primary function and wireless capabilities.

## Tech Stack

*   **Language:** Python
*   **Framework:** Flask & Flask-CORS
*   **Data Handling:** Pandas
*   **Machine Learning:** Scikit-learn
*   **Production Server:** Gunicorn
*   **Deployment:** Render (via Docker)

## Running Locally

**Prerequisites:**
*   Anaconda or Miniconda is recommended for environment management.

**Setup:**

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MdEhsanulHaqueKanan/processor-recommendation-api.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd processor-recommendation-api
    ```
3.  **Create and activate the Conda environment:**
    ```bash
    # Create the environment
    conda create --name processor-api python=3.10

    # Activate the environment
    conda activate processor-api
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the Flask server:**
    ```bash
    flask run
    ```
The API will be available at `http://127.0.0.1:5000`.

[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask-shield]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[Scikit-learn-shield]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[Scikit-learn-url]: https://scikit-learn.org/
[Render-shield]: https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white
[Render-url]: https://render.com/
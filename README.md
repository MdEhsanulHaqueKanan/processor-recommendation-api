# 🧠 Processor Recommendation API (Backend)

[![Python][Python-shield]][Python-url]
[![Flask][Flask-shield]][Flask-url]
[![Scikit-learn][Scikit-learn-shield]][Scikit-learn-url]
[![Render][Render-shield]][Render-url]

This repository contains the **Flask REST API backend** for the Processor Analysis Engine, a full-stack, decoupled machine learning application.

### Project Overview

This API serves as the "brain" for the project. It loads a dataset of over 1,000 processors and serves two machine learning models. **These models are the result of a complete ML workflow built from scratch**, which included data cleaning, extensive feature engineering from raw text fields, and systematic hyperparameter tuning to achieve 92.7% accuracy.

The API exposes JSON-based endpoints to handle two key functions:
1.  **Rule-Based Filtering:** Dynamically filters the processor dataset based on user-defined criteria.
2.  **ML-Powered Prediction:** Predicts a processor's primary function (multi-class) and its wireless capabilities (multi-label) from its specifications.

This backend is designed as a standalone microservice, containerized with Docker, and deployed on Render.

### 🔗 Project Links

| Link                               | URL                                                                                                         |
| :--------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| 🚀 **Live Demo**                   | **[processor-analysis-frontend.vercel.app](https://processor-analysis-frontend.vercel.app/)** |
| 🎨 **Frontend Repository (React)** | [github.com/MdEhsanulHaqueKanan/processor-analysis-frontend](https://github.com/MdEhsanulHaqueKanan/processor-analysis-frontend) |
| ⚙️ **Backend API Repository (This Repo)** | [github.com/MdEhsanulHaqueKanan/processor-recommendation-api](https://github.com/MdEhsanulHaqueKanan/processor-recommendation-api)       |
| 📦 **Original Monolithic Project** | [github.com/MdEhsanulHaqueKanan/processor-recommendation-engine](https://github.com/MdEhsanulHaqueKanan/processor-recommendation-engine) |

*(Note: The server may spin down after inactivity. Please allow up to a minute for the app to "wake up".)*

### Tech Stack

*   **Language:** Python
*   **Framework:** Flask & Flask-CORS
*   **Machine Learning:** Scikit-learn, Pandas
*   **Production Server:** Gunicorn
*   **Deployment:** Render (via Docker)

[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask-shield]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[Scikit-learn-shield]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[Scikit-learn-url]: https://scikit-learn.org/
[Render-shield]: https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white
[Render-url]: https://render.com/

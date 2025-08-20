# 🧠 Processor Recommendation API (Backend)

[![Python][Python-shield]][Python-url]
[![Flask][Flask-shield]][Flask-url]
[![Scikit-learn][Scikit-learn-shield]][Scikit-learn-url]
[![Render][Render-shield]][Render-url]

This repository contains the **Flask REST API backend** for the Processor Analysis Engine, a full-stack, decoupled machine learning application.

### Project Overview

This API serves as the "brain" for the project. It loads a dataset of over 1,000 processors and two custom-trained Scikit-learn models. It exposes JSON-based endpoints to handle two key functions:
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

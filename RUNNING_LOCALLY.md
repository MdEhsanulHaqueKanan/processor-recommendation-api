Running the Full-Stack Processor Analysis Engine Locally
========================================================

This guide provides step-by-step instructions to run the complete full-stack application, which includes the Python/Flask backend API and the React frontend user interface.

Prerequisites
-------------

Before you begin, ensure you have the following software installed on your system:

*   **Anaconda:** For managing the Python environment and its dependencies.
    
*   **Node.js and npm:** For managing the React environment and its dependencies.
    

Project Structure
-----------------

This project consists of two main parts located in separate folders:

1.  **Backend (Flask API):**F:\\ai full stack apps from my ml ai projects\\downloaded from github\\processor-recommendation-engine-main
    
2.  **Frontend (React UI):**F:\\ai full stack apps from my ml ai projects\\downloaded from ai studio\\processor-analysis-frontend
    

You will need **two separate terminals** running simultaneously to operate the application.

Step 1: Run the Backend (Flask API)
-----------------------------------

1.  **Open the Anaconda Prompt.**
    
2.  conda activate G:\\conda\_envs\\processorrecomenginedownloadedgithub
    
3.  cd "F:\\ai full stack apps from my ml ai projects\\downloaded from github\\processor-recommendation-engine-main"
    
4.  flask run
    

The terminal should show that the server is running on http://127.0.0.1:5000.

**Leave this terminal open and running.**

Step 2: Run the Frontend (React UI)
-----------------------------------

1.  **Open a new, separate terminal.** (You can use the regular Command Prompt, PowerShell, or another Anaconda Prompt).
    
2.  cd "F:\\ai full stack apps from my ml ai projects\\downloaded from ai studio\\processor-analysis-frontend"
    
3.  npm install
    
4.  npm run dev
    

The terminal should show that the server is running on http://localhost:5173.

**Leave this second terminal open and running.**

Step 3: Access the Application
------------------------------

You're all set! With both servers running, you can now use the application.

1.  Open your web browser (Chrome, Firefox, etc.).
    
2.  Navigate to the frontend's address: [**http://localhost:5173**](https://www.google.com/url?sa=E&q=http://localhost:5173)
    

The web application will load, and it will automatically communicate with your backend API running on port 5000. You can now use both the "Recommendation Engine" and the "AI Processor Analyzer" tabs.
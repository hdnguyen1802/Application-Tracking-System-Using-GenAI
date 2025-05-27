# AI-Powered ATS Resume Evaluator

This project is a Streamlit web application that uses Google's Vertex AI (Gemini) to evaluate resumes against job descriptions. It acts as an Applicant Tracking System (ATS) tailored for tech roles (Data Scientist, AI Engineer, ML Engineer) in the Hong Kong job market.

The application provides:
1.  A job description match percentage.
2.  A list of missing keywords.
3.  A concise profile summary from the resume.
4.  Actionable feedback to improve the resume for the Hong Kong market.

## Demo

[Watch the Demo Here](https://drive.google.com/file/d/1iv9HbMcZbffSOZ1Fd3MvagZd9uO6SMNv/view?usp=sharing)

## Setup

1.  **Clone the repository.**
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Google Cloud Credentials:**
    * In `main.py`, update the following placeholders:
        * `key_path`: Set this to the file path of your Google Cloud service account key JSON file.
        * `PROJECT_ID`: Set this to your Google Cloud Project ID.
        * Ensure the `LOCATION` (e.g., "us-central1") is correctly set for your Vertex AI resources.

## How to Run

1.  Ensure you have completed the setup steps, including configuring your Google Cloud credentials.
2.  Open your terminal and navigate to the project directory.
3.  Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```
4.  Open the provided URL in your web browser.
5.  Upload your resume (PDF) and paste the job description to get the evaluation.

## Key Dependencies

* Streamlit
* Vertex AI SDK
* PyPDF2

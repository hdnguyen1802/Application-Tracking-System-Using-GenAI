import os
import streamlit as st
import vertexai
import PyPDF2 as pdf
from vertexai.generative_models import GenerativeModel


key_path = r'' # <= Put your Google Cloud service account key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
PROJECT_ID = "" # <= Put your project id of Google Cloud service
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID,location=LOCATION)

model = GenerativeModel("gemini-2.5-pro-preview-05-06")

def pdf_to_text(pdf_files):
    reader = pdf.PdfReader(pdf_files)
    text = ""
    for page_object in reader.pages:
        text += str(page_object.extract_text())
    return text

input_prompt = """
Act as a skilled ATS (Application Tracking System) with deep understanding of the tech field (Data Scientist, AI Engineer, ML Engineer) and the Hong Kong job market.
Your task is to evaluate the provided resume against the given job description. Consider that the Hong Kong job market for these roles is highly competitive.

Provide the following:
1. A job description match percentage.
2. A list of missing keywords from the job description (high accuracy).
3. A concise profile summary based on the resume.
4. Detailed, actionable feedback points to help improve the resume, focusing on alignment with typical expectations in Hong Kong. The feedback should be specific and constructive.

I want the response in one single JSON string. The JSON object must have the following exact keys and structure:
{{ 
  "Job_description_match": "percentage_string (e.g., 75%)",
  "Missing_Keywords": ["keyword1", "keyword2", "..." ],
  "Profile_Summary": "summary_string",
  "Actionable_Feedback": [
    {{ 
      "point": "Title of Feedback Point 1 (e.g., Gain RPA Exposure)", "details": "Detailed advice for point 1..." 
    }}, 
    {{ 
      "point": "Title of Feedback Point 2 (e.g., Focus on Automated Testing)", "details": "Detailed advice for point 2..." 
    }} 
  ]
}} 

Ensure the actionable feedback includes relevant advice, potentially covering areas like RPA exposure, automated testing skills, DevOps/MLOps practices, profile tailoring for specific roles, showcasing domain interest (e.g., railway, finance), relevant certifications, and project enhancements for a stronger profile in the Hong Kong market.

Resume:
{text}

Job Description:
{job_description}
"""

# Steamlit 

st.set_page_config(layout="wide", page_title="ATS Resume Evaluator")

st.title('🎯 Application Tracking System Resume Evaluator')
st.markdown("""
Welcome! This tool leverages AI to analyze your resume against a job description.
It's designed to help you identify areas for improvement, especially for the competitive Hong Kong tech job market.
""")
st.markdown("---")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.header("📄 Upload Your Resume")
        resume_upload = st.file_uploader('Upload your resume (PDF format only)', type=['pdf'], help='Please upload your resume in PDF format.')
    
    with col2:
        st.header("📝 Paste Job Description")
        job_description = st.text_area('Paste the full job description here', height=350, help='Paste the job description you are applying for.')


st.markdown("---")
submit = st.button('🚀 Evaluate My Resume', type="primary", use_container_width=True)

if submit:
    if resume_upload:
        if job_description: # Also check if job description is provided
            text = pdf_to_text(resume_upload)
            full_input = input_prompt.format(text = text, job_description = job_description)
            response = model.generate_content(full_input)
            final_response = response.text
            final_response = final_response[len("```json"):]
            final_response = final_response[:-len("```")]
            final_response = final_response.strip()

            st.subheader("📊 Evaluation Results:")
            st.json(final_response) 
        else:
            st.warning("⚠️ Please paste the job description.")
    else:
        st.warning("⚠️ Please upload your resume.")
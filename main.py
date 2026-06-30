import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq
from pypdf import PdfReader

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_text(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes documents clearly and concisely."
            },
            {
                "role": "user",
                "content": f"Summarize the following text in a few key points:\n\n{text}"
            }
        ]
    )
    return response.choices[0].message.content


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text


# --- Web app interface starts here ---
st.title("📄 PDF Summarizer")
st.write("Upload a PDF and get an instant AI-generated summary.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Reading your PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Generating summary..."):
        summary = summarize_text(pdf_text)

    st.subheader("Summary")
    st.write(summary)








import streamlit as st
import requests

backend_url = "http://localhost:8000"

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: #f0f0f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        min-height: 100vh;
        padding: 20px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff7e5f, #feb47b);
        color: white;
        border-radius: 12px;
        padding: 12px 28px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 126, 95, 0.6);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #feb47b, #ff7e5f);
        box-shadow: 0 6px 20px rgba(254, 180, 123, 0.8);
        transform: scale(1.05);
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: none;
        padding: 12px;
        font-size: 18px;
        box-shadow: inset 0 0 8px rgba(255, 255, 255, 0.2);
        background-color: rgba(255, 255, 255, 0.1);
        color: #f0f0f0;
        transition: background-color 0.3s ease;
    }
    .stTextInput>div>div>input:focus {
        background-color: rgba(255, 255, 255, 0.3);
        outline: none;
    }
    .stTextArea>div>textarea {
        border-radius: 12px;
        border: none;
        padding: 12px;
        font-size: 18px;
        box-shadow: inset 0 0 8px rgba(255, 255, 255, 0.2);
        background-color: rgba(255, 255, 255, 0.1);
        color: #f0f0f0;
        transition: background-color 0.3s ease;
    }
    .stTextArea>div>textarea:focus {
        background-color: rgba(255, 255, 255, 0.3);
        outline: none;
    }
    .stNumberInput>div>input {
        border-radius: 12px;
        border: none;
        padding: 12px;
        font-size: 18px;
        width: 120px;
        box-shadow: inset 0 0 8px rgba(255, 255, 255, 0.2);
        background-color: rgba(255, 255, 255, 0.1);
        color: #f0f0f0;
        transition: background-color 0.3s ease;
    }
    .stNumberInput>div>input:focus {
        background-color: rgba(255, 255, 255, 0.3);
        outline: none;
    }
    .output-container {
        background-color: rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        margin-top: 15px;
        font-family: monospace;
        white-space: pre-wrap;
        color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

import streamlit as st

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'landing'

# Landing Page
def landing_page():
    st.markdown(
        """
        <style>
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .animated-text {
            animation: fadeInUp 1s ease-out forwards;
            opacity: 0;
        }
        .animated-text:nth-child(1) { animation-delay: 0s; }
        .animated-text:nth-child(2) { animation-delay: 0.2s; }
        .animated-text:nth-child(3) { animation-delay: 0.4s; }
        .animated-text:nth-child(4) { animation-delay: 0.6s; }
        </style>
        <div style="text-align: center; padding: 50px 20px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 15px; margin-bottom: 30px;">
            <h1 class="animated-text" style="font-size: 3em; margin-bottom: 10px;">Welcome to Drug Interaction Detection System</h1>
            <p class="animated-text" style="font-size: 1.2em; margin-bottom: 20px;">Advanced AI-powered tool for detecting drug interactions, dosages, and alternatives using NLP and machine learning.</p>
            <div class="animated-text" style="font-size: 4em; margin-bottom: 20px;">💊🔍</div>
            <p class="animated-text" style="font-size: 1em;">This system helps healthcare professionals and patients identify potential drug interactions, get accurate dosage recommendations based on age, and suggest safer alternatives.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Get Started", key="get_started"):
            st.session_state.page = 'app'

def main_app():
    st.title("Features")

if st.session_state.page == 'landing':
    landing_page()
else:
    main_app()

# NLP Extraction
st.header("Extract Drug Information from Text")
text = st.text_area("Enter medical text:")
if st.button("Extract"):
    response = requests.post(f"{backend_url}/extract_drugs", json={"text": text})
    if response.status_code == 200:
        extracted_info = response.json()["extracted_info"]
        try:
            drugs = eval(extracted_info)  # Since it's a string representation of list
            for drug in drugs:
                st.write(f"name : {drug.get('name', 'N/A')}")
                st.write(f"dosage : {drug.get('dosage', 'N/A')}")
                st.write(f"frequency : {drug.get('frequency', 'N/A')}")
                st.write("")
        except:
            st.text(extracted_info)
    else:
        st.error("Error extracting info")

# Image to Text Extraction
st.header("Extract Prescription from Image")
uploaded_file = st.file_uploader("Upload prescription image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    if st.button("Extract Text from Image"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(f"{backend_url}/extract_text_from_image", files=files)
        if response.status_code == 200:
            st.markdown(f'<div class="output-container">{response.json()["extracted_text"]}</div>', unsafe_allow_html=True)
        else:
            st.error("Error extracting text from image")

# Interaction Check
st.header("Check Drug Interactions")
drugs = st.text_input("Enter drugs separated by comma:").split(",")
if st.button("Check Interactions"):
    response = requests.post(f"{backend_url}/check_interactions", json={"drugs": drugs})
    if response.status_code == 200:
        st.markdown(f'<div class="output-container">{response.json()["interactions"]}</div>', unsafe_allow_html=True)
    else:
        st.error("Error checking interactions")

# Dosage
st.header("Get Dosage Recommendation")
drug = st.text_input("Drug name:")
age = st.number_input("Age:", min_value=0)
if st.button("Get Dosage"):
    response = requests.post(f"{backend_url}/get_dosage", json={"drug": drug, "age": age})
    if response.status_code == 200:
        st.markdown(f'<div class="output-container">{response.json()["dosage"]}</div>', unsafe_allow_html=True)
    else:
        st.error("Error getting dosage")

# Alternatives
st.header("Suggest Alternatives")
if st.button("Suggest Alternatives"):
    response = requests.post(f"{backend_url}/suggest_alternatives", json={"drug": drug, "age": age})
    if response.status_code == 200:
        st.markdown(f'<div class="output-container">{response.json()["alternatives"]}</div>', unsafe_allow_html=True)
    else:
        st.error("Error suggesting alternatives")

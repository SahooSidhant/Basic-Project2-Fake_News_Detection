import streamlit as st
import joblib
import re
import base64
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide"
)

# ---------------- BACKGROUND IMAGE ----------------
def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = None
if os.path.exists("background.jpg"):
    bg = get_base64("background.jpg")

# ---------------- LOAD MODEL (CACHED) ----------------
@st.cache_resource
def load_model():
    model = joblib.load("models/linear_svm_model.pkl")
    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# ---------------- CLEAN TEXT ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ---------------- SESSION FIX (NEW - ONLY ADDITION) ----------------
if "news_input" not in st.session_state:
    st.session_state.news_input = ""

def sync_text():
    st.session_state.news_text = st.session_state.news_input

# ---------------- CSS (UNCHANGED + ONLY RESULT FIX) ----------------
st.markdown(
    f"""
    <style>

    .stApp {{
        {"background-image: url('data:image/jpg;base64," + bg + "');" if bg else ""}
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.25);
        z-index: -1;
    }}

    .main .block-container {{
        padding-top: 1rem;
        max-width: 1100px;
    }}

    h1 {{
        color: #161616 !important;
        font-family: Georgia, serif !important;
        font-size: 5rem !important;
        text-align: center !important;
        font-weight: 900 !important;
        margin-top: 0rem !important;
        margin-bottom: 0.1rem !important;
        padding-top: 0rem !important;
    }}

    .subtitle {{
        color: #2b1b12 !important;
        text-align: center !important;
        font-size: 2rem;
        font-family: Georgia, serif;
        font-style: italic;
        font-weight: bold;
        margin-bottom: 2rem;
        
    }}

    [data-testid="stMarkdownContainer"] {{
        text-align: center;
    }}

    [data-testid="stMarkdownContainer"] p {{
        color: #492000 !important;
        font-size: 1.2rem !important;
        font-weight: bold;
    }}

    label {{
        color: #2a1a10 !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }}

    textarea {{
        background-color: #1e1e1e !important;
        color: #ffffff !important;
        border: 2px solid #d4af37 !important;
        border-radius: 12px !important;
        font-size: 18px !important;
        font-family: Georgia, serif !important;
    }}

    textarea::placeholder {{
        color: #bbbbbb !important;
    }}

    .stButton > button {{
        background: #d4af37 !important;
        color: #111111 !important;
        border: none !important;
        border-radius: 12px !important;
        font-size: 20px !important;
        font-weight: bold !important;
    }}

    .stButton > button:hover {{
        background: #e6c75c !important;
        color: black !important;
    }}

    /* ---------------- RESULT FIX (IMPROVED VISIBILITY ONLY) ---------------- */
    .result-box {{
        margin-top: 15px;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        text-shadow: 1px 1px 2px black;
    }}

    .fake {{
        background: rgba(255, 0, 0, 0.25);
        border: 2px solid red;
        color: #FF0000;

    }}

    .real {{
        background: rgba(0, 255, 100, 0.20);
        border: 2px solid #00c853;
        color: #00e676;
    }}

    /* ---------------- FOOTER (UNCHANGED) ---------------- */
    .footer {{
        display: inline-block;
        margin: 25px auto 0 auto;
        padding: 8px 14px;
        text-align: center;
        color: #ffffff;
        font-family: Georgia, serif;
        font-size: 16px;
        font-style: italic;
        font-weight: bold;
        background: rgba(0,0,0,0.85);
        border-radius: 10px;
    }}

    footer {{
        visibility: hidden;
    }}

    #MainMenu, header {{
        visibility: hidden;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.markdown("<h1>THE DAILY TRUTH</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="subtitle">
        Fake News Detection Using Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- INPUT (FIXED LIVE UPDATE) ----------------
col1, col2, col3 = st.columns([1.5, 3, 1.5])

with col2:
    news_text = st.text_area(
        "Paste a news article below and let the model determine whether it is likely 'FAKE' or 'REAL'",
        height=220,
        key="news_input",
        on_change=sync_text
    )

# ---------------- BUTTON ----------------
with col2:
    predict = st.button(
        "🔍 Analyze Article",
        use_container_width=True,
        disabled=(news_text.strip() == "")
    )

# ---------------- PREDICT ----------------
with col2:
    if predict:

        cleaned_text = clean_text(news_text)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]

        if prediction == 0:
            st.markdown(
                "<div class='result-box fake'>🚨 FAKE NEWS DETECTED</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                "<div class='result-box real'>✅ REAL NEWS DETECTED</div>",
                unsafe_allow_html=True
            )

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>Fake News Detection Project → SIDHANTA SAHOO</div>",
    unsafe_allow_html=True
)
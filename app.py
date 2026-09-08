import streamlit as st
from datetime import datetime
from pathlib import Path
import time

# Настройка страницы
st.set_page_config(
    page_title="IPTT News Monitor",
    page_icon="🔬",
    layout="wide"
)

# Кастомные стили
st.markdown("""
    <style>
    .main-header {
        font-size: 24px;
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 0px;
    }
    .news-card {
        background: #FFFFFF;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        border-left: 4px solid #5B7C3E;
    }
    .news-title {
        font-size: 16px;
        font-weight: 600;
        color: #1F2937;
        margin-bottom: 8px;
    }
    .news-meta {
        font-size: 12px;
        color: #6B7280;
        margin-bottom: 8px;
    }
    .news-snippet {
        font-size: 14px;
        color: #6B7280;
        line-height: 1.5;
    }
    .stButton>button {
        background-color: #5B7C3E;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 6px;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #4a6632;
    }
    [data-testid="stSidebar"] .stButton>button {
        background-color: #5B7C3E;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 6px;
        font-weight: 500;
        width: 100%;
    }
    [data-testid="stSidebar"] .stButton>button:hover {
        background-color: #4a6632;
    }
    [data-testid="stMain"] {
        background-color: #f1f8e9;
    }
    </style>
""", unsafe_allow_html=True)

# === Шапка: логотип + название + дата ===
logo_path = "logo_combined.png"
col1, col2, col3 = st.columns([2, 5, 2])

with col1:
    if Path(logo_path).exists():
        st.image(logo_path, width=400)
    else:
        st.markdown("🔬")

with col2:
    st.markdown('<p class="main-header">IPTT News Monitor</p>', unsafe_allow_html=True)

with col3:
    st.markdown(
        f"<p style='text-align: right; color: #6B7280; font-size: 13px; padding-top: 12px;'>"
        f"📅 {datetime

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
        margin

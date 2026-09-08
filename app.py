import streamlit as st
from datetime import datetime
from pathlib import Path
import time

st.set_page_config(page_title="IPTT News Monitor", page_icon="", layout="wide")

st.markdown("""
<style>
.main-header {font-size: 24px; font-weight: 600; color: #1F2937; margin-bottom: 0px;}
.news-card {background: #FFFFFF; border-radius: 8px; padding: 15px; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.08); border-left: 4px solid #5B7C3E;}
.news-title {font-size: 16px; font-weight: 600; color: #1F2937; margin-bottom: 8px;}
.news-meta {font-size: 12px; color: #6B7280; margin-bottom: 8px;}
.news-snippet {font-size: 14px; color: #6B7280; line-height: 1.5;}
[data-testid="stMain"] {background-color: #c5e1a5;}
</style>
""", unsafe_allow_html=True)

logo_path = "logo_combined.png"
if Path(logo_path).exists():
    st.image(logo_path, width=900)

col_title, col_date = st.columns([8, 2])
with col_title:
    st.markdown('<p class="main-header">IPTT News Monitor</p>', unsafe_allow_html=True)
with col_date:
    date_str = datetime.now().strftime("%d.%m.%Y")
    st.markdown(f"<p style='text-align: right; color: #6B7280; font-size: 13px;'>{date_str}</p>", unsafe_allow_html=True)

st.markdown("---")

with st.sidebar:
    st.header("Настройки поиска")
    search_clicked = st.button("Запустить поиск", use_container_width=True)
    keywords = st.text_input("Ключевые слова", value="пектин, пищевые волокна")
    source = st.selectbox("Источник поиска", ["Google News", "Яндекс Новости", "Все источники"], index=0)
    custom_source = st.text_input("Добавить источник", value="")
    period = st.selectbox("Период", ["Сегодня", "Неделя", "Месяц", "Год"], index=1)
    limit = st.slider("Количество новостей", 5, 50, 10)
    
    st.markdown("---")
    if "show_links" not in st.session_state:
        st.session_state.show_links = False
    if st.button("Ссылки на проект", use_container_width=True):
        st.session_state.show_links = not st.session_state.show_links
    if st.session_state.show_links:
        st.markdown("#### Основные ресурсы:")
        st.markdown("- [PectinWorld](https://pectinworld.com/)")
        st.markdown("- [Университет 2035](https://pt.2035.university/project/sozdanie-promyslennogo-proizvodstva-pektina-i-pisevyh-volokon_2021_05_28_04_41_27#pulse260038)")
        st.markdown("#### Платформы:")
        st.markdown("- [BRICS Awards](https://bricsawards.tech/practices/18402)")
        st.markdown("- [РСХБ/Цифра](https://rshbdigital.ru/ekspertiza-i-tekhnologii/almanah/startups/promyshlennoe-proizvodstvo-pektina-i-pishhevykh-volokon)")
    
    st.markdown("---")
    st.info("Поиск новостей по ключевым словам")

st.markdown("### Свежие новости")

if search_clicked:
    progress_bar = st.progress(0)
    status_text = st.empty()
    try:
        status_text.text("Инициализация...")
        progress_bar.progress(25)
        time.sleep(0.5)
        status_text.text("Поиск...")
        progress_bar.progress(50)
        time.sleep(0.5)
        status_text.text("Анализ...")
        progress_bar.progress(75)
        time.sleep(0.5)
        news_items = []
        progress_bar.progress(100)
        status_text.text("Готово!")
        time.sleep(0.5)
        progress_bar.empty()
        status_text.empty()
        
        if news_items:
           

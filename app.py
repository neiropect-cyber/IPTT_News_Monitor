import streamlit as st
from datetime import datetime
from pathlib import Path
import time

st.set_page_config(page_title="IPTT News Monitor", page_icon="", layout="wide")

st.markdown("""
<style>
.main-header {font-size: 24px; font-weight: 600; color: #1F2937;}
.news-card {background: #FFFFFF; border-radius: 8px; padding: 15px; margin-bottom: 15px; border-left: 4px solid #5B7C3E;}
[data-testid="stMain"] {background-color: #c5e1a5;}
</style>
""", unsafe_allow_html=True)

col_logo, col_title, col_date = st.columns([3, 5, 2])

with col_logo:
    if Path("logo_combined.png").exists():
        st.image("logo_combined.png", width=250)

with col_title:
    st.markdown('<p class="main-header">IPTT News Monitor</p>', unsafe_allow_html=True)

with col_date:
    st.markdown(f"<p style='text-align:right;color:#6B7280;font-size:13px;'>{datetime.now().strftime('%d.%m.%Y')}</p>", unsafe_allow_html=True)

st.markdown("---")

with st.sidebar:
    st.header("Настройки")
    search_clicked = st.button("Запустить поиск", use_container_width=True)
    keywords = st.text_input("Ключевые слова", value="пектин, пищевые волокна")
    add_source = st.text_input("Добавить источник", value="")
    
    if add_source:
        source_options = ["Google News", "Яндекс Новости", "Все источники", add_source]
    else:
        source_options = ["Google News", "Яндекс Новости", "Все источники"]
    
    source = st.selectbox("Источник", source_options)
    period = st.selectbox("Период", ["Сегодня", "Неделя", "Месяц", "Год"])
    limit = st.slider("Количество", 5, 50, 10)
    
    st.markdown("---")
    
    if "show_links" not in st.session_state:
        st.session_state.show_links = False
    
    if st.button("Ссылки", use_container_width=True):
        st.session_state.show_links = not st.session_state.show_links
    
    if st.session_state.show_links:
        st.markdown("- [PectinWorld](https://pectinworld.com/)")
        st.markdown("- [Университет 2035](https://pt.2035.university/project/sozdanie-promyslennogo-proizvodstva-pektina-i-pisevyh-volokon_2021_05_28_04_41_27)")

st.markdown("### Новости")

if search_clicked:
    with st.spinner("Ищу..."):
        time.sleep(1)
        news_items = []
    if news_items:
        st.success(f"Найдено: {len(news_items)}")
        for item in news_items:
            st.markdown(f"<div class='news-card'><b>{item.get('title')}</b><br><small>{item.get('date')}</small><p>{item.get('snippet')}</p></div>", unsafe_allow_html=True)
    else:
        st.warning("Ничего не найдено")
else:
    st.info("Нажмите кнопку

import streamlit as st
from datetime import datetime
from pathlib import Path
import time

# Настройка страницы
st.set_page_config(
    page_title="IPTT News Monitor",
    page_icon="",
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
    </style>
""", unsafe_allow_html=True)

# === Шапка: логотип + название + дата ===
logo_path = "logo_combined.png"
col1, col2, col3 = st.columns([1, 6, 2])

with col1:
    if Path(logo_path).exists():
        st.image(logo_path, width=120)
    else:
        st.markdown("🔬")

with col2:
    st.markdown('<p class="main-header">IPTT News Monitor</p>', unsafe_allow_html=True)

with col3:
    st.markdown(
        f"<p style='text-align: right; color: #6B7280; font-size: 13px; padding-top: 12px;'>"
        f"📅 {datetime.now().strftime('%d.%m.%Y')}</p>",
        unsafe_allow_html=True
    )

st.markdown("---")

# Боковая панель с настройками
with st.sidebar:
    st.header("🔧 Настройки поиска")
    
    keywords = st.text_input(
        "Ключевые слова",
        value="пектин, пищевые волокна",
        help="Введите ключевые слова через запятую"
    )
    
    source = st.selectbox(
        "Источник",
        ["Google News", "Яндекс Новости", "Все источники"],
        index=0
    )
    
    period = st.selectbox(
        "Период",
        ["Сегодня", "Неделя", "Месяц", "Год"],
        index=1
    )
    
    limit = st.slider("Количество новостей", 5, 50, 10)
    
    # === Кнопка со ссылками ===
    st.markdown("---")
    
    if st.button("🔗 Ссылки на проект", use_container_width=True):
        st.markdown("#### 📌 Основные ресурсы:")
        st.markdown("– [PectinWorld](https://pectinworld.com/)")
        st.markdown("– [Университет 2035](https://pt.2035.university/project/sozdanie-promyslennogo-proizvodstva-pektina-i-pisevyh-volokon_2021_05_28_04_41_27#pulse260038)")
        
        st.markdown("####  Платформы и конкурсы:")
        st.markdown("– [BRICS Awards](https://bricsawards.tech/practices/18402)")
        st.markdown("– [Сильные идеи](https://xn--d1ach8g.xn--c1aenmdblfega.xn--p1ai/improject-145438/ideas/211734)")
        st.markdown("– [РСХБ/Цифра](https://rshbdigital.ru/ekspertiza-i-tekhnologii/almanah/startups/promyshlennoe-proizvodstvo-pektina-i-pishhevykh-volokon)")
        st.markdown("– [Радар НТИ](https://pt.u2035test.ru/project/sozdanie-promyslennogo-proizvodstva-pektina-i-pisevyh-volokon_2021_05_28_04_41_27)")
        st.markdown("– [АТР Каталог технологий](https://atr.gov.ru/tech/623041940492)")
        
        st.markdown("#### 📺 Видео и медиа:")
        st.markdown("– [Дзен канал РИАЦ 34](https://dzen.ru/a/Za9RopsN-Bbk_oAT)")
        st.markdown("– [Видео на Rutube](https://rutube.ru/video/21d1e3ed5b92f8b2a09d6e9334feab0c/)")
        st.markdown("– [Видео на Яндекс](https://ya.ru/video/preview/11803489309973110150)")
    
    st.markdown("---")
    st.markdown("### О сервисе")
    st.info("Поиск новостей по заданным ключевым словам из различных источников")
    
    search_clicked = st.button("🔍 Запустить поиск", use_container_width=True)

# Основная область
st.markdown("### 📰 Свежие новости")

if search_clicked:
    # Индикатор загрузки
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        status_text.text("Инициализация поиска...")
        progress_bar.progress(25)
        time.sleep(0.5)
        
        status_text.text("Поиск источников...")
        progress_bar.progress(50)
        time.sleep(0.5)
        
        status_text.text("Анализ результатов...")
        progress_bar.progress(75)
        time.sleep(0.5)
        
        # Заглушка для демонстрации
        news_items = []
        
        progress_bar.progress(100)
        status_text.text("Готово!")
        time.sleep(0.5)
        
        progress_bar.empty()
        status_text.empty()
        
        if news_items:
            st.success(f"Найдено {len(news_items)} новостей")
            
            for item in news_items:
                st.markdown(f"""
                    <div class="news-card">
                        <div class="news-title">{item.get('title', 'Заголовок')}</div>
                        <div class="news-meta">
                             {item.get('date', 'Дата не указана')} | 
                            🔗 {item.get('source', 'Источник')}
                        </div>
                        <div class="news-snippet">{item.get('snippet', 'Описание')}</div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("📭 Ничего не найдено")
            st.info("💡 Попробуйте:\n– Расширить период поиска\n– Изменить ключевые слова\n– Выбрать другой источник")
            
    except Exception as e:
        st.error(f"❌ Ошибка при поиске: {str(e)}")
        st.info("Проверьте подключение к интернету и повторите попытку")

else:
    st.info("Нажмите кнопку в меню слева, чтобы начать поиск новостей")

# Футер
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #6B7280; font-size: 12px;'>
        IPTT News Monitor · 2026 · Версия 1.0
    </div>
    """, 
    unsafe_allow_html=True
)

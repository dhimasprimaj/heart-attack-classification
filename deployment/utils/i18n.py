import json
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
@st.cache_data
def load_translations():
    with open(BASE_DIR / "translations.json", encoding="utf-8") as f:
        return json.load(f)
    
translations = load_translations()

def init_language():
    if "lang" not in st.session_state:
        st.session_state.lang = "en"

def language_switcher():
    lang_map = {
        "English": "en",
        "Indonesia": "id"
    }

    selected = st.sidebar.selectbox(
        tr("language"),
        options=list(lang_map.keys()),
        index=list(lang_map.values()).index(st.session_state.lang)
    )
    new_lang = lang_map[selected]
    
    if new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.rerun()

def tr(key):
    return translations[st.session_state.lang].get(key, key)
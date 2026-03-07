import streamlit as st
from utils.i18n import init_language, language_switcher, tr

init_language()
language_switcher()

st.set_page_config(
    page_title=tr("page_title"),
    page_icon="❤️"
)

pg = st.navigation({
    "Main": [
        st.Page("pages/index.py", title=tr("landing"), icon=":material/home:"),
        st.Page("pages/predict_new_model.py", title=tr("predict_new"), icon=":material/edit:"),
        st.Page("pages/predict_old_model.py", title=tr("predict_old"), icon=":material/edit:"),
    ],
    "About": [
        st.Page("pages/about_new_model.py", title=tr("new_model"), icon=":material/smart_toy:"),
        st.Page("pages/about_old_model.py", title=tr("old_model"), icon=":material/smart_toy:"),
        st.Page("pages/team.py", title=tr("team"), icon=":material/diversity_1:"),
    ],
})

pg.run()
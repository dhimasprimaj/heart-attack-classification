import streamlit as st
from utils.i18n import tr

st.title("🫀 "+tr("title"), text_alignment="center",anchor=False)

st.subheader(tr("index_title_desc"), anchor=False)

st.warning(
    tr("index_warning")
)

st.markdown(tr("index_what"))

st.markdown(tr("index_how"))

if st.button("👉 "+tr("index_button"), width="stretch"):
    st.switch_page("pages/predict_new_model.py")
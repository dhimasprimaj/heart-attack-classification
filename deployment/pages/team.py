import streamlit as st
from utils.i18n import tr
st.set_page_config(page_title=tr("team"), layout="centered")

st.title(tr("contributors"), anchor=False, width="stretch", text_alignment="center")
c1,c2 = st.columns(2)
with c1:
    st.subheader("Dhimas Primajaya",text_alignment="center", anchor=False)
    st.subheader("Jackson",text_alignment="center", anchor=False)
with c2:
    st.subheader("Reynold Kunarto",text_alignment="center", anchor=False)
    st.subheader("Rijki Hardiyanti",text_alignment="center", anchor=False)
st.subheader("Zufar Bagas P.",text_alignment="center", anchor=False)

st.markdown(
    "<h2 style='text-align:center'><a href='https://github.com/Pattern-Seeker/heart-attack-classification'>Project Repo</a></h2>",
    unsafe_allow_html=True
)
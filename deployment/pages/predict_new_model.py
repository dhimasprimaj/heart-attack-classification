import streamlit as st
import pandas as pd
from components.input_form import input_form
from utils.encoders_loader import load_new_encoders as load_encoders
from utils.model_loader import load_new_model as load_model
from utils.input_preprocessor import preprocess_input
from utils.i18n import tr

st.set_page_config(page_title="Input Data", layout="centered",page_icon="✏️")

data = input_form(False)

if data is not None:
    # Load artifacts (cached)
    label_encoders, onehot_encoder = load_encoders()
    model = load_model()

    # Dict → DataFrame
    input_df = pd.DataFrame([data])
    # Preprocess
    X = preprocess_input(input_df, label_encoders, onehot_encoder)
    # Predict
    prediction = model.predict(X)[0]
    proba = model.predict_proba(X)[0]

    # Output
    st.subheader(tr("prediction_result"))

    if prediction == 1:
        st.error("⚠️ "+tr("high_risk_heart_attack"))
    else:
        st.success("✅ "+tr("low_risk_heart_attack"))

    st.metric(
        label=tr("confidence"),
        value=f"{max(proba)*100:.2f}%"
    )

    st.write({
        tr("high_risk_prob"): f"{proba[1]*100:.2f}%",
        tr("low_risk_prob"): f"{proba[0]*100:.2f}%"
    })
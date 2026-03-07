import streamlit as st
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

@st.cache_resource
def load_old_model():
    with open(BASE_DIR / "models" / "tuned_rocauc_model_Logistic Regression.pkl", "rb") as f:
        model = pickle.load(f)
    
    return model

@st.cache_resource
def load_new_model():
    with open(BASE_DIR / "models" / "unsupervised" / "model_best_rocauc_logistic_regression_unsupervised.pkl", "rb") as f:
        model = pickle.load(f)
    
    return model
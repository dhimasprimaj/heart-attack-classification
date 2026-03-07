import streamlit as st
import re
from utils.i18n import tr

def is_valid_bp_format(bp: str) -> bool:
    bp = bp.strip()
    pattern = r"^\d{2,3}/\d{2,3}$"
    return bool(re.match(pattern, bp))

def extract_bp(bp: str):
    if not is_valid_bp_format(bp):
        return None, None
    systolic, diastolic = bp.split("/")
    return int(systolic), int(diastolic)
gender_labels = {
    "Male": tr("male"),
    "Female": tr("female")
}
diet_labels = {
    "Healthy": tr("diet_healthy"),
    "Average": tr("diet_average"),
    "Unhealthy": tr("diet_unhealthy"),
}

countries = [
    "South Korea", "Nigeria", "United States", "Colombia", "Thailand",
    "Australia", "Argentina", "Germany", "Canada", "China", "Brazil",
    "France", "United Kingdom", "Spain", "Vietnam", "New Zealand",
    "South Africa", "Japan", "Italy", "India", "Other",
]
obesity_bmi_threshold = 30.0
countries.sort()

def is_form_valid(
    age, height, weight, country, blood_pressure, triglycerides, heart_rate, cholesterol, diet, use_country=True
):
    return (
        age > 0
        and height > 0
        and weight > 0
        and triglycerides > 0
        and heart_rate > 0
        and cholesterol > 0
        and (country is not None if use_country else True)
        and diet is not None
        and is_valid_bp_format(blood_pressure)
    )

def input_form(use_country: bool = True):
    with st.form("input_form"):
        st.subheader(tr("form_general_info"), divider="gray", anchor=False)
        a1, a2 = st.columns(2)
        with a1:
            age = st.number_input(tr("age"), min_value=1, value=20)
            height = st.number_input(
                tr("height"), min_value=1.0, value=170.0,
                placeholder=tr("height_placeholder")
            )
        with a2:
            sex = st.radio(
                tr("gender"),
                options=list(gender_labels.keys()),
                format_func=lambda x: gender_labels[x],
                horizontal=True
            )
            weight = st.number_input(
                tr("weight"), min_value=1.0, value=55.0,
                placeholder=tr("weight_placeholder")
            )

        if use_country:
            country = st.selectbox(
                tr("country"), countries, index=None,
                placeholder=tr("country_placeholder")
            )
            if country is None:
                st.warning(tr("country_warning"))
        else:
            country = None

        st.subheader(tr("form_medical_info"), divider="gray", anchor=False)
        b1, b2 = st.columns(2)
        with b1:
            blood_pressure = st.text_input(
                tr("blood_pressure"), placeholder=tr("blood_pressure_example")
            )
            if blood_pressure and not is_valid_bp_format(blood_pressure):
                st.warning(tr("blood_pressure_warning"))
            triglycerides = st.number_input(tr("triglycerides"), min_value=0, value=150)
            diabetes = st.checkbox(tr("diabetes"))
            family_history = st.checkbox(tr("family_history"))
            smoking = st.checkbox(tr("smoker"))
        with b2:
            heart_rate = st.number_input(tr("heart_rate"), min_value=1, value=75)
            cholesterol = st.number_input(tr("cholesterol"), min_value=1, value=200)
            alcohol_consumption = st.checkbox(tr("alcohol_consumer"))
            previous_heart_problems = st.checkbox(tr("previous_heart_problems"))
            medication_use = st.checkbox(tr("medication_use"))

        st.subheader(tr("form_lifestyle_info"), divider="gray", anchor=False)
        diet = st.selectbox(
            tr("diet_type"),
            options=list(diet_labels.keys()),   # internal values
            format_func=lambda x: diet_labels[x],  # translated display
            index=None,
            placeholder=tr("diet_placeholder")
        )
        stress_level = st.slider(tr("stress_level"), min_value=1, max_value=10, value=5)
        physical_activity_days_per_week = st.slider(tr("physical_activity"), min_value=0, max_value=7, value=3)
        sleep_hours_per_day = st.slider(tr("sleep_duration"), min_value=0.0, max_value=24.0, value=7.0, step=0.5)
        exercise_hours_per_week = st.slider(tr("exercise_per_week"), min_value=0.0, value=4.0, max_value=24.0 * 7.0, step=0.25)
        sedentary_hours_per_day = st.slider(tr("sedentary_time"), min_value=0.0, max_value=24.0, value=6.0, step=0.5)

        submitted = st.form_submit_button(
            tr("submit"), icon=":material/send:", icon_position="right", width="stretch"
        )

    if submitted:
        valid = is_form_valid(
            age=age, height=height, weight=weight, country=country,
            blood_pressure=blood_pressure, triglycerides=triglycerides,
            heart_rate=heart_rate, cholesterol=cholesterol, diet=diet,
            use_country=use_country
        )
        if valid:
            st.success(tr("submitted"))
            bmi = weight / (height * height / 10000.0)
            obesity = bmi > obesity_bmi_threshold
            sys, dia = extract_bp(blood_pressure)

            data = {
                "Age": age, "Sex": sex, "Cholesterol": cholesterol,
                "Heart Rate": heart_rate, "Diabetes": diabetes,
                "Family History": family_history, "Smoking": smoking,
                "Blood Pressure": blood_pressure, "Obesity": obesity,
                "Alcohol Consumption": alcohol_consumption,
                "Exercise Hours Per Week": exercise_hours_per_week,
                "Diet": diet, "Previous Heart Problems": previous_heart_problems,
                "Medication Use": medication_use, "Stress Level": stress_level,
                "Sedentary Hours Per Day": sedentary_hours_per_day, "BMI": bmi,
                "Triglycerides": triglycerides,
                "Physical Activity Days Per Week": physical_activity_days_per_week,
                "Sleep Hours Per Day": sleep_hours_per_day,
                "Country": country, "BP-Systolic": sys, "BP-Diastolic": dia,
            }
            return data
        else:
            st.error(tr("error_validate"))
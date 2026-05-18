import streamlit as st

# =========================================================
# PAIN POINT OPTIONS
# =========================================================

PAIN_POINTS = [
    "Scrap",
    "Rework",
    "FPY",
    "PPM",
    "8D",
    "Safety",
    "Innovation",
    "Other"
]

# =========================================================
# SUBMISSION FORM
# =========================================================

def submission_form():

    with st.form("pain_point_form"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input("Name")

            plant = st.text_input("Plant")

            area = st.text_input("Area")

            process = st.text_input("Process")

        with col2:

            pain_point = st.selectbox(
                "Pain Point",
                PAIN_POINTS
            )

            safety_risk = st.selectbox(
                "Safety Risk?",
                ["No", "Yes"]
            )

        suggested_improvement = st.text_area(
            "Suggested Improvement"
        )

        uploaded_photo = st.file_uploader(
            "Photo Upload",
            type=["png", "jpg", "jpeg"]
        )

        submitted = st.form_submit_button("SAVE")

    return {
        "submitted": submitted,
        "name": name,
        "plant": plant,
        "area": area,
        "process": process,
        "pain_point": pain_point,
        "suggested_improvement": suggested_improvement,
        "safety_risk": safety_risk,
        "uploaded_photo": uploaded_photo
    }
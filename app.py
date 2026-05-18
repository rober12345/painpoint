import streamlit as st
import pandas as pd

from PIL import Image

from modules.database import (
    create_table,
    get_connection
)

from modules.forms import submission_form

from modules.dashboard import show_dashboard

from modules.utilities import (
    create_folders,
    save_photo
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PAIN POINT",
    layout="wide"
)

# =========================================================
# INITIAL SETUP
# =========================================================

create_folders()

create_table()

conn = get_connection()

# =========================================================
# HEADER WITH LOGO
# =========================================================

logo = Image.open("assets/logo.png")

col1, col2 = st.columns([1, 5])

with col1:

    st.image(
        logo,
        width=140
    )

with col2:

    st.title("PAIN POINT")

    st.subheader(
        "Operational Intelligence & Innovation Hub"
    )

st.markdown("""
Capture operational pain points,
innovation opportunities,
safety risks,
and improvement ideas across all plants.
""")

# =========================================================
# FORM
# =========================================================

form_data = submission_form()

# =========================================================
# SAVE DATA
# =========================================================

if form_data["submitted"]:

    photo_path = save_photo(
        form_data["uploaded_photo"]
    )

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO submissions (

        timestamp,
        name,
        plant,
        area,
        process,
        pain_point,
        suggested_improvement,
        safety_risk,
        photo_path

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        pd.Timestamp.now(),

        form_data["name"],
        form_data["plant"],
        form_data["area"],
        form_data["process"],
        form_data["pain_point"],
        form_data["suggested_improvement"],
        form_data["safety_risk"],
        photo_path

    ))

    conn.commit()

    st.success(
        "Submission saved successfully."
    )

# =========================================================
# LOAD DATABASE
# =========================================================

query = """
SELECT * FROM submissions
ORDER BY id DESC
"""

submissions_df = pd.read_sql_query(
    query,
    conn
)

# =========================================================
# SHOW DASHBOARD
# =========================================================

show_dashboard(submissions_df)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "PAIN POINT — Operational Visibility Platform"
)
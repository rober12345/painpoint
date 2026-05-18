import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# DASHBOARD FUNCTION
# =========================================================

def show_dashboard(df):

    st.divider()

    st.header("Operational Dashboard")

    # =====================================================
    # EMPTY CHECK
    # =====================================================

    if df.empty:

        st.warning(
            "No submissions available."
        )

        return

    # =====================================================
    # METRICS
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Submissions",
            len(df)
        )

    with col2:

        st.metric(
            "Plants Reporting",
            df["plant"].nunique()
        )

    with col3:

        st.metric(
            "Safety Risks",
            len(
                df[
                    df["safety_risk"] == "Yes"
                ]
            )
        )

    with col4:

        st.metric(
            "Innovation Ideas",
            len(
                df[
                    df["pain_point"] == "Innovation"
                ]
            )
        )

    # =====================================================
    # PARETO CHART
    # =====================================================

    st.subheader("Pain Point Distribution")

    pareto = (
        df["pain_point"]
        .value_counts()
        .reset_index()
    )

    pareto.columns = [
        "Pain Point",
        "Count"
    ]

    fig_pareto = px.bar(
        pareto,
        x="Pain Point",
        y="Count",
        title="Pain Point Pareto"
    )

    st.plotly_chart(
        fig_pareto,
        use_container_width=True
    )

    # =====================================================
    # PLANT ANALYSIS
    # =====================================================

    st.subheader("Submissions by Plant")

    plant_data = (
        df["plant"]
        .value_counts()
        .reset_index()
    )

    plant_data.columns = [
        "Plant",
        "Count"
    ]

    fig_plant = px.bar(
        plant_data,
        x="Plant",
        y="Count",
        title="Plant Participation"
    )

    st.plotly_chart(
        fig_plant,
        use_container_width=True
    )

    # =====================================================
    # DATA TABLE
    # =====================================================

    st.subheader("All Submissions")

    st.dataframe(
        df,
        use_container_width=True
    )
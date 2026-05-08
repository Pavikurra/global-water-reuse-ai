import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Global Water Reuse AI",
    layout="wide"
)

st.title("Global Water Reuse AI")

st.write(
    "Open-data and machine learning platform for estimating global greywater "
    "production, reuse effectiveness, and water reuse opportunity by country."
)

uploaded_file = st.file_uploader(
    "Upload global_ml_predictions.csv",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Countries/Regions",
        len(df)
    )

    col2.metric(
        "Total Estimated Greywater Tons/Hour",
        f"{df['greywater_tons_per_hour'].sum():,.0f}"
    )

    col3.metric(
        "Total Untapped Reuse m³/year",
        f"{df['untapped_reuse_m3_year'].sum():,.0f}"
    )

st.subheader("Global Greywater Production Map")

fig_map = px.choropleth(
    df,
    locations="iso3",
    color="greywater_tons_per_hour",
    hover_name="country",
    color_continuous_scale="Blues",
    title="Estimated Greywater Tons Per Hour by Country"
)

st.plotly_chart(fig_map, use_container_width=True)

st.subheader("Predicted Reuse Effectiveness Map")

fig_class = px.choropleth(
    df,
    locations="iso3",
    color="predicted_reuse_class",
    hover_name="country",
    title="Predicted Greywater Reuse Effectiveness by Country"
)

st.plotly_chart(fig_class, use_container_width=True)


    
    st.subheader("Top Countries by Greywater Tons/Hour")

    top_greywater = df.sort_values(
        by="greywater_tons_per_hour",
        ascending=False
    ).head(10)

    st.dataframe(
        top_greywater[
            [
                "country",
                "population",
                "greywater_tons_per_hour",
                "reuse_effectiveness_class",
                "predicted_reuse_class"
            ]
        ]
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        top_greywater["country"],
        top_greywater["greywater_tons_per_hour"]
    )

    ax.set_title("Top Countries by Estimated Greywater Tons/Hour")
    ax.set_ylabel("Tons per Hour")
    ax.tick_params(axis="x", rotation=45)

    st.pyplot(fig)

    st.subheader("Countries With Highest Untapped Reuse Opportunity")

    top_untapped = df.sort_values(
        by="untapped_reuse_m3_year",
        ascending=False
    ).head(10)

    st.dataframe(
        top_untapped[
            [
                "country",
                "untapped_reuse_m3_year",
                "reuse_efficiency_pct",
                "reuse_effectiveness_class"
            ]
        ]
    )

    st.subheader("Filter by Predicted Reuse Class")

    selected_class = st.selectbox(
        "Select reuse class",
        df["predicted_reuse_class"].dropna().unique()
    )

    filtered_df = df[
        df["predicted_reuse_class"] == selected_class
    ]

    st.dataframe(
        filtered_df[
            [
                "country",
                "population",
                "greywater_tons_per_hour",
                "reuse_efficiency_pct",
                "predicted_reuse_class"
            ]
        ]
    )

else:
    st.info(
        "Upload the global_ml_predictions.csv file generated from the ML notebook."
    )

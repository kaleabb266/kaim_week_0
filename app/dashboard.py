import streamlit as st
from analysis_tools import (
    load_data, clean_data, plot_time_series, plot_correlation_heatmap, wind_rose_plot,
    plot_rh_vs_temp, plot_histograms, z_score_analysis, bubble_chart
)

# File Paths
datasets = {
    "Benin - Malanville": "../data/benin-malanville.csv",
    "Sierra Leone - Bumbuna": "../data/sierraleone-bumbuna.csv",
    "Togo - Dapaong-QC": "../data/togo-dapaong_qc.csv"
}

# Sidebar
st.sidebar.title("Select Dataset")
dataset_choice = st.sidebar.selectbox("Choose a dataset", list(datasets.keys()))
file_path = datasets[dataset_choice]

# Main Section
st.title("Solar Radiation Data Analysis Dashboard")

# Load and Clean Data
st.subheader("Load and Clean Data")
data = load_data(file_path)
columns_to_check = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust', 'Precipitation']
data_cleaned = clean_data(data, columns_to_check)

st.write("Dataset Preview:")
st.dataframe(data_cleaned.head())

# Placeholder for displaying analysis
analysis_output = st.empty()

# Analysis Options
analysis_choice = st.sidebar.selectbox("Choose Analysis", [
    "Time Series Plot",
    "Correlation Heatmap",
    "Wind Analysis",
    "Temperature Analysis",
    "Histograms",
    "Z-Score Analysis",
    "Bubble Chart"
])

# Display appropriate analysis
if analysis_choice == "Time Series Plot":
    with analysis_output:
        plot_time_series(data_cleaned, "GHI", "GHI Over Time", "Time", "GHI (W/m²)")

elif analysis_choice == "Correlation Heatmap":
    with analysis_output:
        columns_to_correlate = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS', 'TModA', 'TModB']
        plot_correlation_heatmap(data_cleaned, columns_to_correlate)

elif analysis_choice == "Wind Analysis":
    with analysis_output:
        wind_rose_plot(data_cleaned)

elif analysis_choice == "Temperature Analysis":
    with analysis_output:
        plot_rh_vs_temp(data_cleaned)

elif analysis_choice == "Histograms":
    with analysis_output:
        variables = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb']
        plot_histograms(data_cleaned, variables)

elif analysis_choice == "Z-Score Analysis":
    with analysis_output:
        anomalies = z_score_analysis(data_cleaned, "GHI")
        st.write("Number of anomalies detected:", len(anomalies))
        st.write("Anomalies:", anomalies)

elif analysis_choice == "Bubble Chart":
    with analysis_output:
        bubble_chart(data_cleaned)

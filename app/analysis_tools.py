import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from windrose import WindroseAxes
import seaborn as sns
from scipy.stats import zscore

# Load Dataset
def load_data(file_path):
    """Loads the dataset and returns a pandas DataFrame."""
    data = pd.read_csv(file_path)
    return data

# Data Cleaning
def clean_data(data, columns_to_check):
    """Cleans the dataset by removing negative values and handling missing values."""
    # Remove rows with negative values in the specified columns
    data_cleaned = data[(data[columns_to_check] >= 0).all(axis=1)]
    
    # Handle missing values only in numeric columns
    numeric_columns = data_cleaned.select_dtypes(include=[np.number]).columns
    data_cleaned[numeric_columns] = data_cleaned[numeric_columns].fillna(data_cleaned[numeric_columns].median())
    
    return data_cleaned


# Time Series Plot
def plot_time_series(data, column, title, xlabel, ylabel):
    """Plots a time series for the specified column."""
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp', inplace=True)
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data[column], label=f'{column} over time')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

# Correlation Heatmap
def plot_correlation_heatmap(data, columns):
    """Plots a correlation heatmap for specified columns."""
    correlation_matrix = data[columns].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

# Wind Rose
def wind_rose_plot(data):
    """Plots a wind rose for Wind Direction and Wind Speed."""
    ax = WindroseAxes.from_ax()
    ax.bar(data['WD'], data['WS'], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend(title="Wind Speed (m/s)")
    plt.title("Wind Rose")
    plt.show()

# Scatter Plot for RH vs Temperature
def plot_rh_vs_temp(data):
    """Plots RH vs Temperature with GHI as a hue."""
    sns.scatterplot(x=data['RH'], y=data['Tamb'], hue=data['GHI'], palette='coolwarm')
    plt.title("RH vs Temperature with GHI as hue")
    plt.xlabel("Relative Humidity (%)")
    plt.ylabel("Temperature (°C)")
    plt.show()

# Histograms
def plot_histograms(data, variables):
    """Plots histograms for specified variables."""
    for var in variables:
        plt.hist(data[var].dropna(), bins=30, alpha=0.7, label=var)
        plt.title(f"Histogram of {var}")
        plt.xlabel(var)
        plt.ylabel("Frequency")
        plt.show()

# Z-Score Analysis
def z_score_analysis(data, column):
    """Performs Z-Score analysis and flags anomalies."""
    data[f'{column}_Z'] = zscore(data[column])
    anomalies = data[np.abs(data[f'{column}_Z']) > 3]
    return anomalies

# Bubble Chart
def bubble_chart(data):
    """Plots a bubble chart for GHI vs Tamb vs WS with RH as bubble size."""
    plt.scatter(data['Tamb'], data['GHI'], s=data['RH'], alpha=0.5, label="RH size")
    plt.title("GHI vs Tamb vs WS (Bubble size = RH)")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Global Horizontal Irradiance (GHI)")
    plt.show()

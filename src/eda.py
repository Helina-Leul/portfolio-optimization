"""
eda.py

Exploratory Data Analysis (EDA) utilities for financial time series.

This module provides reusable visualization and analysis functions for:
- Price trends
- Daily returns
- Rolling statistics
- Volatility analysis
- Distribution analysis
- Correlation analysis
- Outlier detection

Author: Helina Leul
Project: Time Series Forecasting for Portfolio Management Optimization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# 1. Plot Closing Price
# ---------------------------------------------------------
def plot_closing_price(df: pd.DataFrame, ticker: str):
    """
    Plot adjusted closing price over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Adj Close"], label=f"{ticker} Close Price")

    plt.title(f"{ticker} Closing Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


# ---------------------------------------------------------
# 2. Plot Daily Returns
# ---------------------------------------------------------
def plot_daily_returns(df: pd.DataFrame, ticker: str):
    """
    Plot daily percentage returns.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Daily Return"], color="purple")

    plt.title(f"{ticker} Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.axhline(0, linestyle="--", color="black", linewidth=1)
    plt.show()


# ---------------------------------------------------------
# 3. Plot Rolling Statistics
# ---------------------------------------------------------
def plot_rolling_statistics(df: pd.DataFrame, ticker: str):
    """
    Plot rolling mean and rolling standard deviation.
    """
    plt.figure(figsize=(12, 6))

    plt.plot(df["Date"], df["Adj Close"], label="Price", alpha=0.5)
    plt.plot(df["Date"], df["Rolling Mean"], label="Rolling Mean (30D)")
    plt.plot(df["Date"], df["Rolling Std"], label="Rolling Std (30D)")

    plt.title(f"{ticker} Rolling Statistics")
    plt.xlabel("Date")
    plt.legend()
    plt.show()


# ---------------------------------------------------------
# 4. Distribution of Returns
# ---------------------------------------------------------
def plot_return_distribution(df: pd.DataFrame, ticker: str):
    """
    Plot histogram of daily returns.
    """
    plt.figure(figsize=(10, 5))

    sns.histplot(df["Daily Return"], bins=50, kde=True)

    plt.title(f"{ticker} Daily Return Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.show()


# ---------------------------------------------------------
# 5. Correlation Heatmap (multiple assets)
# ---------------------------------------------------------
def plot_correlation_heatmap(df_dict: dict):
    """
    Plot correlation heatmap of adjusted close prices.

    Parameters:
    df_dict : dict
        Dictionary of dataframes {ticker: dataframe}
    """
    combined = pd.DataFrame()

    for ticker, df in df_dict.items():
        combined[ticker] = df["Adj Close"].values

    corr = combined.corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")

    plt.title("Asset Correlation Heatmap")
    plt.show()


# ---------------------------------------------------------
# 6. Outlier Detection (Z-score method)
# ---------------------------------------------------------
def detect_outliers(df: pd.DataFrame, ticker: str, threshold: float = 3):
    """
    Detect outliers in daily returns using Z-score.
    """
    returns = df["Daily Return"]

    z_scores = (returns - returns.mean()) / returns.std()

    outliers = df[np.abs(z_scores) > threshold]

    print(f"\n{ticker} Outliers detected: {len(outliers)}")

    return outliers


# ---------------------------------------------------------
# 7. Volatility Plot
# ---------------------------------------------------------
def plot_volatility(df: pd.DataFrame, ticker: str, window: int = 30):
    """
    Plot rolling volatility (standard deviation of returns).
    """
    volatility = df["Daily Return"].rolling(window).std()

    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], volatility)

    plt.title(f"{ticker} {window}-Day Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.show()

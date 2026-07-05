"""
preprocessing.py

Utility functions for preprocessing financial time series data.

This module provides reusable functions for:
- Cleaning financial datasets
- Calculating daily returns
- Calculating rolling statistics
- Saving processed datasets

Author: Helina Leul
Project: Time Series Forecasting for Portfolio Management Optimization
"""

from pathlib import Path

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess a financial time series dataframe.

    Parameters
    ----------
    df : pd.DataFrame
        Raw financial dataframe.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe.
    """

    # Create a copy to avoid modifying the original dataframe
    df = df.copy()

    # ---------------------------------------------------------
    # Convert Date column to datetime
    # ---------------------------------------------------------
    df["Date"] = pd.to_datetime(df["Date"])

    # ---------------------------------------------------------
    # Sort chronologically
    # ---------------------------------------------------------
    df = df.sort_values("Date")

    # ---------------------------------------------------------
    # Reset index
    # ---------------------------------------------------------
    df = df.reset_index(drop=True)

    # ---------------------------------------------------------
    # Remove duplicate rows
    # ---------------------------------------------------------
    df = df.drop_duplicates()

    # ---------------------------------------------------------
    # Ensure numeric columns are numeric
    # ---------------------------------------------------------
    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # ---------------------------------------------------------
    # Handle missing values
    # ---------------------------------------------------------
    df = df.ffill()
    df = df.bfill()

    return df


def calculate_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily percentage returns.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    df = df.copy()

    df["Daily Return"] = df["Adj Close"].pct_change()

    df["Daily Return"] = df["Daily Return"].fillna(0)

    return df


def calculate_rolling_statistics(
    df: pd.DataFrame,
    window: int = 30
) -> pd.DataFrame:
    """
    Calculate rolling mean and rolling standard deviation.

    Parameters
    ----------
    df : pd.DataFrame

    window : int
        Rolling window size.

    Returns
    -------
    pd.DataFrame
    """

    df = df.copy()

    df["Rolling Mean"] = (
        df["Adj Close"]
        .rolling(window=window)
        .mean()
    )

    df["Rolling Std"] = (
        df["Adj Close"]
        .rolling(window=window)
        .std()
    )

    return df


def normalize_prices(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize Adjusted Close prices using Min-Max Scaling.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    df = df.copy()

    scaler = MinMaxScaler()

    df["Normalized Close"] = scaler.fit_transform(
        df[["Adj Close"]]
    )

    return df


def check_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Return missing value counts.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.Series
    """

    return df.isnull().sum()


def save_processed_data(
    df: pd.DataFrame,
    ticker: str
) -> None:
    """
    Save processed dataframe to the project's data/processed folder.

    Parameters
    ----------
    df : pd.DataFrame
        Processed dataframe.

    ticker : str
        Asset ticker.
    """

    # Get project root directory
    project_root = Path(__file__).resolve().parent.parent

    # Create data/processed directory
    output_path = project_root / "data" / "processed"

    output_path.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save file
    file_path = output_path / f"{ticker}_processed.csv"

    df.to_csv(file_path, index=False)

    print(f"✓ Saved processed {ticker} data to:\n{file_path}")


def load_processed_data(file_path: str) -> pd.DataFrame:
    """
    Load a processed dataset.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    pd.DataFrame
    """

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])

    return df

"""
data_loader.py

Clean and robust utility module for downloading, saving,
and loading financial data from Yahoo Finance.

This version:
- Fixes MultiIndex columns from yfinance
- Standardizes column names
- Uses project-root–safe paths
- Ensures reproducibility across notebook/script usage
"""

from pathlib import Path
import pandas as pd
import yfinance as yf


# -------------------------------------------------------
# Get project root (important for correct file saving)
# -------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent


# -------------------------------------------------------
# 1. Download Data
# -------------------------------------------------------
def download_data(
    ticker: str,
    start_date: str,
    end_date: str
) -> pd.DataFrame:
    """
    Download historical stock/ETF data from Yahoo Finance
    and clean column structure.

    Returns:
        Clean DataFrame with standard columns:
        Date, Open, High, Low, Close, Adj Close, Volume
    """

    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=False
    )

    if df.empty:
        raise ValueError(f"No data found for ticker: {ticker}")

    # -------------------------------
    # FIX 1: Handle MultiIndex columns
    # -------------------------------
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # -------------------------------
    # Reset index to get Date column
    # -------------------------------
    df.reset_index(inplace=True)

    # -------------------------------
    # Ensure correct column order
    # -------------------------------
    expected_cols = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    df = df[expected_cols]

    return df


# -------------------------------------------------------
# 2. Save Data
# -------------------------------------------------------
def save_data(
    df: pd.DataFrame,
    ticker: str,
    output_dir: str = "data/raw"
) -> None:
    """
    Save DataFrame to CSV inside project directory.
    """

    output_path = PROJECT_ROOT / output_dir
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / f"{ticker}.csv"

    df.to_csv(file_path, index=False)

    print(f"✓ Saved {ticker} data to {file_path}")


# -------------------------------------------------------
# 3. Load Data
# -------------------------------------------------------
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV file into DataFrame.
    """

    return pd.read_csv(file_path)


# -------------------------------------------------------
# 4. Download Multiple Assets
# -------------------------------------------------------
def download_multiple_assets(
    tickers: list,
    start_date: str,
    end_date: str,
    output_dir: str = "data/raw"
) -> dict:
    """
    Download multiple assets, clean them, and save automatically.

    Returns:
        Dictionary of DataFrames
    """

    datasets = {}

    for ticker in tickers:
        print(f"\nDownloading {ticker}...")

        df = download_data(
            ticker=ticker,
            start_date=start_date,
            end_date=end_date
        )

        save_data(
            df=df,
            ticker=ticker,
            output_dir=output_dir
        )

        datasets[ticker] = df

    print("\n✓ All datasets downloaded successfully.")

    return datasets

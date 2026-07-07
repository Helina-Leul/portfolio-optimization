# Time Series Forecasting for Portfolio Management Optimization

## Project Overview

This project develops a complete **data-driven portfolio management framework** for **GMF Investments** by combining financial data analysis, time series forecasting, portfolio optimization, and strategy backtesting.

The objective is to use historical market data and predictive modeling techniques to generate investment insights, optimize asset allocation, and evaluate whether a model-driven portfolio strategy can outperform a traditional benchmark portfolio.

The project focuses on three financial assets with different risk characteristics:

* **TSLA (Tesla Inc.)** — High-growth, high-volatility equity asset
* **SPY (S&P 500 ETF)** — Broad market exposure and moderate risk
* **BND (Vanguard Total Bond Market ETF)** — Low-risk fixed-income asset

The complete workflow includes:

* Financial data acquisition using Yahoo Finance
* Data preprocessing and exploratory analysis
* Statistical and deep learning forecasting models
* Future market trend analysis
* Modern Portfolio Theory (MPT) optimization
* Efficient Frontier analysis
* Portfolio backtesting against a benchmark strategy

---

# Business Objective

GMF Investments aims to improve investment decision-making by integrating forecasting models and portfolio optimization techniques.

The project addresses the following business questions:

* How have TSLA, SPY, and BND historically behaved?
* Can historical price patterns provide useful forecasting signals?
* Which forecasting model performs better for Tesla price prediction?
* How can forecast insights improve portfolio allocation?
* Does the optimized portfolio outperform a traditional investment strategy?

---

# Dataset

## Data Source

Historical financial data was collected using:

* **Yahoo Finance API**
* Python `yfinance` library

## Assets

| Asset             | Ticker | Description                             | Risk Profile            |
| ----------------- | ------ | --------------------------------------- | ----------------------- |
| Tesla             | TSLA   | Electric vehicle and technology company | High Risk / High Return |
| S&P 500 ETF       | SPY    | Tracks the S&P 500 Index                | Medium Risk             |
| Vanguard Bond ETF | BND    | Investment-grade bond market exposure   | Low Risk                |

## Time Period

```
January 1, 2015 - June 30, 2026
```

## Main Features

The dataset contains:

* Date
* Open Price
* High Price
* Low Price
* Closing Price
* Adjusted Closing Price
* Trading Volume

---

# Project Workflow

The project follows a complete financial analytics pipeline:

```
Financial Data Collection
          |
          ↓
Data Cleaning & Preprocessing
          |
          ↓
Exploratory Data Analysis
          |
          ↓
Risk Analysis & Stationarity Testing
          |
          ↓
Time Series Forecasting
          |
          ↓
Portfolio Optimization
          |
          ↓
Strategy Backtesting
          |
          ↓
Investment Insights
```

---

# Task 1 — Data Preprocessing and Exploratory Data Analysis

## Data Preparation

The following preprocessing steps were performed:

* Data extraction using Yahoo Finance
* Missing value detection and handling
* Data type validation
* Date indexing and sorting
* Daily return calculation
* Rolling statistics generation

## Exploratory Data Analysis

The analysis included:

### Price Trend Analysis

Analyzed historical adjusted closing prices to understand long-term trends.

Key observations:

* TSLA demonstrated significant growth with high volatility.
* SPY showed steady long-term market growth.
* BND provided stability with lower price fluctuations.

### Daily Return Analysis

Calculated daily percentage returns to analyze:

* Market fluctuations
* Volatility behavior
* Risk characteristics

### Rolling Statistics

Calculated:

* Rolling mean
* Rolling standard deviation
* Rolling volatility

### Correlation Analysis

Analyzed relationships between assets using correlation and covariance analysis.

Findings:

* TSLA and SPY showed stronger relationship due to equity exposure.
* BND provided diversification benefits due to lower correlation with equities.

### Stationarity Testing

The Augmented Dickey-Fuller (ADF) test was applied.

Purpose:

* Determine whether financial time series are stationary.
* Understand suitability for ARIMA modeling.

Results:

* Stock prices were found to be non-stationary.
* Differencing was required before ARIMA modeling.

---

# Task 2 — Time Series Forecasting

Two forecasting approaches were implemented:

## 1. ARIMA Model

### Purpose

ARIMA was used as a classical statistical forecasting approach.

Configuration:

```
ARIMA(5,1,0)
```

Features:

* Handles non-stationary data through differencing
* Provides interpretable statistical forecasting
* Generates confidence intervals

## 2. LSTM Neural Network

### Purpose

A Long Short-Term Memory network was implemented to capture complex sequential patterns.

Architecture:

```
Input Sequence
      |
LSTM Layer (64 units)
      |
Dropout
      |
LSTM Layer (32 units)
      |
Dropout
      |
Dense Layer
      |
Price Prediction
```

Sequence Design:

* Previous 60 trading days used as input
* Next day adjusted close predicted

## Model Evaluation

Models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Percentage Error (MAPE)

Model comparison was performed to identify the most suitable forecasting approach for Tesla price prediction.

---

# Task 3 — Future Market Trend Forecasting

The best-performing forecasting model was used to generate future Tesla price forecasts.

## Forecast Horizon

Approximately:

```
6 Months Future Forecast
(126 Trading Days)
```

## Forecast Analysis Included:

* Future predicted prices
* Confidence intervals
* Forecast uncertainty analysis
* Trend interpretation

## Key Insights

The forecast indicates expected future price behavior while recognizing that uncertainty increases as the prediction horizon expands.

Confidence intervals become wider over time, showing reduced reliability for long-term predictions.

Forecasting models are therefore used as decision-support tools rather than exact price prediction systems.

---

# Task 4 — Portfolio Optimization Using Modern Portfolio Theory

Modern Portfolio Theory (MPT) was applied to construct optimized portfolios.

## Expected Returns

Expected returns were calculated using:

* Forecast-based expected return for TSLA
* Historical average returns for SPY and BND

## Risk Measurement

Calculated:

* Covariance matrix
* Portfolio volatility
* Risk-adjusted returns

## Efficient Frontier

Generated portfolios with different:

* Expected returns
* Risk levels

Two optimal portfolios were identified:

## Maximum Sharpe Ratio Portfolio

Objective:

Maximize risk-adjusted return.

## Minimum Volatility Portfolio

Objective:

Minimize portfolio risk.

Portfolio allocation was analyzed across:

* TSLA
* SPY
* BND

---

# Task 5 — Portfolio Strategy Backtesting

The optimized portfolio was evaluated using historical market data.

## Benchmark

The strategy was compared against:

```
60% SPY + 40% BND
```

A commonly used balanced investment portfolio.

## Performance Metrics

The following metrics were calculated:

### Total Return

Measures overall portfolio growth.

### Annualized Return

Measures yearly performance.

### Sharpe Ratio

Measures return relative to risk.

### Maximum Drawdown

Measures the largest portfolio decline.

## Backtesting Objective

The goal was to determine whether the optimized portfolio could provide improved risk-adjusted performance compared with a passive benchmark strategy.

---

# Technologies Used

## Programming Language

* Python

## Data Analysis

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

## Financial Data

* yfinance

## Statistical Modeling

* Statsmodels
* ARIMA

## Deep Learning

* TensorFlow
* Keras
* LSTM

## Portfolio Optimization

* PyPortfolioOpt

## Machine Learning Evaluation

* Scikit-learn

---

# Repository Structure

```
portfolio-optimization/

│
├── data/
│   └── processed/
│       ├── TSLA_processed.csv
│       ├── SPY_processed.csv
│       └── BND_processed.csv
│
├── notebooks/
│   └── 01_Data_Preprocessing_EDA.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── eda.py
│
├── tests/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# Key Project Outcomes

This project successfully demonstrates:

✅ Financial data engineering workflow
✅ Time series forecasting implementation
✅ ARIMA and LSTM model comparison
✅ Risk analysis and portfolio construction
✅ Efficient Frontier optimization
✅ Investment strategy backtesting

The project provides a complete example of how machine learning and quantitative finance techniques can support modern portfolio management decisions.

---

# Limitations

Although forecasting and optimization models provide valuable insights, financial markets remain highly uncertain.

Limitations include:

* Historical patterns may not repeat in the future.
* External factors such as economic events and company news are not fully captured.
* Forecast accuracy decreases over longer horizons.
* Portfolio optimization depends on assumptions about expected returns and risk.

Therefore, the developed framework should be used as a decision-support system combined with professional financial judgment.

---

# Future Improvements

Potential improvements include:

* Hyperparameter tuning for ARIMA and LSTM models
* Implementing SARIMA models
* Adding more financial indicators:

  * Moving averages
  * RSI
  * MACD
  * Trading volume signals
* Incorporating macroeconomic variables
* Building automated portfolio rebalancing
* Deploying the solution as an interactive dashboard

---

# Author

**Helina Leul**

Software Engineering Student
Data Science & AI Enthusiast

---

# Acknowledgments

This project was completed as part of an AI and Data Science learning challenge focused on:

* Financial analytics
* Machine learning
* Time series forecasting
* Portfolio optimization
* Data-driven investment strategies

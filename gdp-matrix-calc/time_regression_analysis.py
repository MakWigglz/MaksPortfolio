import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Existing GDP calculation code
years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
num_years = len(years)

# Simulated data for demonstration
C = np.random.randint(150, 200, (13, num_years)).sum(axis=0)
I = np.random.randint(50, 80, (14, num_years)).sum(axis=0)
G = np.random.randint(100, 150, (11, num_years)).sum(axis=0)
X = np.random.randint(50, 130, (11, num_years)).sum(axis=0)
M = np.random.randint(80, 200, (11, num_years)).sum(axis=0)
NX = X - M
GDP = C + I + G + NX

# Create DataFrame for analysis
gdp_df = pd.DataFrame({
    'Year': years,
    'Consumption (C)': C,
    'Investment (I)': I,
    'Government Spending (G)': G,
    'Exports (X)': X,
    'Imports (M)': M,
    'Net Exports (NX)': NX,
    'GDP': GDP
}).set_index('Year')

# --- Regression Analysis ---
X = gdp_df[['Consumption (C)', 'Investment (I)', 'Government Spending (G)', 'Net Exports (NX)']]
y = gdp_df['GDP']
X = sm.add_constant(X)  # Adds a constant term to the predictor
model = sm.OLS(y, X).fit()
print(model.summary())

# --- Time Series Analysis ---
plt.figure(figsize=(10, 5))
plt.plot(gdp_df.index, gdp_df['GDP'], marker='o', label='GDP')
plt.title('GDP Over Time')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.grid()
plt.legend()
plt.show()

# --- Panel Data Analysis ---
# For simplicity, we'll use the same data since we have a time series here.
# Normally, you'd have more cross-sectional data.
# Using the same model as above but treating it as panel data for demonstration
panel_model = sm.OLS(y, X).fit()
print(panel_model.summary())

# --- Econometric Modeling ---
# Example: Check for stationarity using ADF test
from statsmodels.tsa.stattools import adfuller

adf_result = adfuller(gdp_df['GDP'])
print(f'ADF Statistic: {adf_result[0]}')
print(f'p-value: {adf_result[1]}')

# Plotting the components of GDP
gdp_df[['Consumption (C)', 'Investment (I)', 'Government Spending (G)', 'Net Exports (NX)']].plot(figsize=(12, 6))
plt.title('GDP Components')
plt.xlabel('Year')
plt.ylabel('Values')
plt.grid()
plt.legend()
plt.show()

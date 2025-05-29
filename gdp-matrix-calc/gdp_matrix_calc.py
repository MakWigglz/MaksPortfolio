import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Define the period of interest
years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
num_years = len(years)

# --- C: Consumption (Personal Consumption Expenditures) ---
# Represents household spending on goods and services.
# 10+ common breakdowns:
C_categories = [
    "Durable Goods: New Vehicles",
    "Durable Goods: Furniture & Appliances",
    "Durable Goods: Recreational Goods",
    "Nondurable Goods: Food & Beverages (at home)",
    "Nondurable Goods: Clothing & Footwear",
    "Nondurable Goods: Gasoline & Energy",
    "Services: Housing & Utilities",
    "Services: Healthcare (incl. medical services & drugs)",
    "Services: Transportation (fares, car rentals)",
    "Services: Food Services & Accommodation",
    "Services: Recreation & Culture",
    "Services: Financial & Insurance",
    "Services: Education"
]
# Simulate data for each category over the years (rows are categories, columns are years)
# Using random values for demonstration, scaled to be roughly proportional to real-world spending
C = np.array([
    np.random.randint(150, 200, num_years),  # New Vehicles
    np.random.randint(100, 140, num_years),  # Furniture & Appliances
    np.random.randint(80, 120, num_years),   # Recreational Goods
    np.random.randint(400, 500, num_years),  # Food & Beverages (at home)
    np.random.randint(120, 180, num_years),  # Clothing & Footwear
    np.random.randint(70, 100, num_years),   # Gasoline & Energy
    np.random.randint(500, 600, num_years),  # Housing & Utilities
    np.random.randint(300, 400, num_years),  # Healthcare
    np.random.randint(90, 130, num_years),   # Transportation Services
    np.random.randint(250, 350, num_years),  # Food Services & Accommodation
    np.random.randint(100, 150, num_years),  # Recreation & Culture
    np.random.randint(60, 90, num_years),    # Financial & Insurance
    np.random.randint(80, 110, num_years)    # Education
])

# --- I: Investment (Gross Private Domestic Investment) ---
# Represents spending by businesses on capital goods, residential construction, and changes in inventories.
# 10+ common breakdowns:
I_categories = [
	"Expat remitances: Social ROI",
    "Nonresidential Structures: Commercial Buildings",
    "Nonresidential Structures: Industrial Buildings",
    "Nonresidential Structures: Other (e.g., oil & gas)",
    "Nonresidential Equipment: Industrial Machinery",
    "Nonresidential Equipment: Information Processing Equip.",
    "Nonresidential Equipment: Transportation Equipment",
    "Intellectual Property Products: Software",
    "Intellectual Property Products: Research & Development",
    "Residential Investment: Single-Family Housing",
    "Residential Investment: Multi-Family Housing",
    "Residential Investment: Improvements",
    "Change in Private Inventories: Manufacturing",
    "Change in Private Inventories: Wholesale/Retail Trade"
]
I = np.array([
	np.random.randint(8, 9, num_years),
    np.random.randint(50, 80, num_years),   # Commercial Buildings
    np.random.randint(40, 70, num_years),   # Industrial Buildings
    np.random.randint(20, 50, num_years),   # Other Nonresidential Structures
    np.random.randint(100, 150, num_years), # Industrial Machinery
    np.random.randint(120, 180, num_years), # Information Processing Equip.
    np.random.randint(60, 90, num_years),   # Transportation Equipment
    np.random.randint(30, 60, num_years),   # Software
    np.random.randint(40, 70, num_years),   # R&D
    np.random.randint(150, 200, num_years), # Single-Family Housing
    np.random.randint(50, 80, num_years),   # Multi-Family Housing
    np.random.randint(30, 60, num_years),   # Improvements
    np.random.randint(-10, 30, num_years),  # Manufacturing Inventories (can be negative)
    np.random.randint(-5, 20, num_years)    # Wholesale/Retail Inventories (can be negative)
])

# --- G: Government Consumption Expenditures and Gross Investment ---
# Represents government spending on goods and services.
# 10+ common breakdowns (can be federal, state, and local combined for simplicity):
G_categories = [
    "Defense: Military Personnel Compensation",
    "Defense: Weapons & Equipment",
    "Defense: Operations & Maintenance",
    "Nondefense: Government Administration (Salaries)",
    "Nondefense: Healthcare Administration",
    "Nondefense: Education Spending (public schools)",
    "Nondefense: Public Safety (Police, Fire)",
    "Nondefense: Transportation Infrastructure",
    "Nondefense: Environmental Protection",
    "Nondefense: Scientific Research",
    "Nondefense: Public Hospitals & Health Programs"
]
G = np.array([
    np.random.randint(100, 150, num_years), # Military Personnel
    np.random.randint(80, 120, num_years),  # Weapons & Equipment
    np.random.randint(70, 110, num_years),  # Operations & Maintenance
    np.random.randint(120, 180, num_years), # Government Administration
    np.random.randint(40, 70, num_years),   # Healthcare Administration
    np.random.randint(150, 200, num_years), # Public Education
    np.random.randint(90, 130, num_years),  # Public Safety
    np.random.randint(60, 100, num_years),  # Transportation Infrastructure
    np.random.randint(20, 40, num_years),   # Environmental Protection
    np.random.randint(30, 60, num_years),   # Scientific Research
    np.random.randint(50, 90, num_years)    # Public Hospitals
])

# --- X: Exports of Goods and Services ---
# Goods and services produced domestically and sold to foreign residents.
# 10+ common breakdowns:
X_categories = [
    "Goods Exports: Agricultural Products",
    "Goods Exports: Machinery & Equipment",
    "Goods Exports: Automotive Products",
    "Goods Exports: Chemicals",
    "Goods Exports: Electronics",
    "Services Exports: Travel (Tourism)",
    "Services Exports: Transportation",
    "Services Exports: Financial Services",
    "Services Exports: Intellectual Property Charges",
    "Services Exports: Computer & Information Services",
    "Services Exports: Other Business Services"
]
X = np.array([
    np.random.randint(50, 80, num_years),   # Agricultural Products
    np.random.randint(90, 130, num_years),  # Machinery & Equipment
    np.random.randint(70, 100, num_years),  # Automotive Products
    np.random.randint(60, 90, num_years),   # Chemicals
    np.random.randint(80, 120, num_years),  # Electronics
    np.random.randint(40, 70, num_years),   # Travel Services
    np.random.randint(30, 50, num_years),   # Transportation Services
    np.random.randint(20, 40, num_years),   # Financial Services
    np.random.randint(15, 30, num_years),   # Intellectual Property
    np.random.randint(25, 45, num_years),   # Computer & Information Services
    np.random.randint(35, 60, num_years)    # Other Business Services
])

# --- M: Imports of Goods and Services ---
# Goods and services produced abroad and purchased by domestic residents.
# 10+ common breakdowns:
M_categories = [
    "Goods Imports: Crude Oil & Petroleum Products",
    "Goods Imports: Manufactured Consumer Goods",
    "Goods Imports: Industrial Supplies & Materials",
    "Goods Imports: Automotive Products",
    "Goods Imports: Capital Goods (Machinery)",
    "Services Imports: Travel (Domestic residents abroad)",
    "Services Imports: Transportation",
    "Services Imports: Financial Services",
    "Services Imports: Intellectual Property Charges",
    "Services Imports: Computer & Information Services",
    "Services Imports: Other Business Services"
]
M = np.array([
    np.random.randint(80, 120, num_years),  # Crude Oil
    np.random.randint(150, 200, num_years), # Manufactured Consumer Goods
    np.random.randint(100, 140, num_years), # Industrial Supplies
    np.random.randint(90, 130, num_years),  # Automotive Products
    np.random.randint(70, 110, num_years),  # Capital Goods
    np.random.randint(50, 80, num_years),   # Travel Services (abroad)
    np.random.randint(35, 60, num_years),   # Transportation Services
    np.random.randint(25, 45, num_years),   # Financial Services
    np.random.randint(20, 35, num_years),   # Intellectual Property
    np.random.randint(30, 50, num_years),   # Computer & Information Services
    np.random.randint(40, 70, num_years)    # Other Business Services
])

# --- Calculate Net Exports ---
# Sum of all export categories - Sum of all import categories for each year
NX = X.sum(axis=0) - M.sum(axis=0)

# --- Calculate GDP ---
# GDP = C + I + G + (X - M)
GDP = C.sum(axis=0) + I.sum(axis=0) + G.sum(axis=0) + NX

# --- Create DataFrames for detailed components ---

# DataFrames for detailed components, making it easier to plot later
df_C_detail = pd.DataFrame(C, index=C_categories, columns=years)
df_I_detail = pd.DataFrame(I, index=I_categories, columns=years)
df_G_detail = pd.DataFrame(G, index=G_categories, columns=years)
df_X_detail = pd.DataFrame(X, index=X_categories, columns=years)
df_M_detail = pd.DataFrame(M, index=M_categories, columns=years)

# Create a DataFrame for the overall GDP and its main components
gdp_summary_df = pd.DataFrame({
    'Year': years,
    'Consumption (C)': C.sum(axis=0),
    'Investment (I)': I.sum(axis=0),
    'Government Spending (G)': G.sum(axis=0),
    'Exports (X)': X.sum(axis=0),
    'Imports (M)': M.sum(axis=0),
    'Net Exports (X-M)': NX,
    'GDP': GDP
}).set_index('Year')

print("--- GDP Summary (Values in Hypothetical Units) ---")
print(gdp_summary_df)

print("\n--- Detailed Consumption (C) Data ---")
print(df_C_detail)

print("\n--- Detailed Investment (I) Data ---")
print(df_I_detail)

print("\n--- Detailed Government Spending (G) Data ---")
print(df_G_detail)

print("\n--- Detailed Exports (X) Data ---")
print(df_X_detail)

print("\n--- Detailed Imports (M) Data ---")
print(df_M_detail)
plt.figure(figsize=(12, 6))
df_C_detail.T.plot(kind='bar', stacked=True, cmap='coolwarm', alpha=0.8)
plt.title("Breakdown of Personal Consumption Expenditures (C)")
plt.xlabel("Year")
plt.ylabel("Spending (Hypothetical Units)")
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.show()
plt.figure(figsize=(10, 6))
sns.heatmap(df_G_detail, cmap='magma', annot=True, fmt='d')
plt.title("Government Spending Breakdown Heatmap")
plt.xlabel("Year")
plt.ylabel("Government Spending Categories")
plt.show()
plt.figure(figsize=(12, 6))
sns.lineplot(data=gdp_summary_df, markers=True, dashes=False)
plt.title("GDP and Economic Component Trends Over Time")
plt.xlabel("Year")
plt.ylabel("Value (Hypothetical Units)")
plt.legend(title="Component", bbox_to_anchor=(1.2, 1))
plt.show()

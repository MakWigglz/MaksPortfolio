import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class DataSource1:
    def __init__(self, file_path):
        """initialize by reading CSV."""
        self.file_path = file_path
        self.data = pd.read_csv(file_path, parse_dates=['Date'])  # load CSV, parse dates
    def get_column(self, column_name):
        """Retrieve data from a column"""
        if column_name in self.data.columns:
            return self.data[column_name]
        else:
            return f"Column '{column_name}' not found"
    def get_row_by_date(self, date):
        if 'Date' in self.data.columns:
            filtered_data = self.data[self.data['Date'] == date]
            return filtered_data if not filtered_data.empty else f"no data found for {date}"
        else:
            return "no 'Date' column"
    def get_summary(self):
        return self.data.describe()
data_manager = DataSource1("stocks.csv")
googl_df = pd.DataFrame(data_manager.get_column("GOOGL"))
aapl_df = pd.DataFrame(data_manager.get_column("AAPL"))
xrx_df = pd.DataFrame(data_manager.get_column("XRX"))

print("Google's Stock DataFrame: ")
print(googl_df.head())
print("Apple and Xerox....")
print(aapl_df.head(35))
print(xrx_df.head(35))

# Mak's numPy arrays
googl_array = googl_df['GOOGL'].to_numpy()
aapl_array = aapl_df['AAPL'].to_numpy()
xrx_array = xrx_df['XRX'].to_numpy()
print(xrx_array, googl_array, aapl_array)

# Plotting Graphs
dates = data_manager.data['Date']
plt.figure(figsize=(20, 10))
plt.plot(dates, aapl_array, label='AAPL')
plt.plot(dates, googl_array, label='GOOGL')
plt.plot(dates, xrx_array, label='XRX')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('AAPL vs GOOGL Stock Prices')
plt.legend()
plt.grid(True)
plt.show()

# Array calculations
price_difference = aapl_array - googl_array
print("\nDifference between AAPL and GOOGL prices:")
print(price_difference)

average_aapl = np.mean(aapl_array)
print(f"\nAverage AAPL price: {average_aapl:.2f}")

max_googl = np.max(googl_array)
print(f"Maximum GOOGL price: {max_googl:.2f}")

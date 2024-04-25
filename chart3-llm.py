import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('dataorders-withnull.csv')

# Convert 'Order Date' column to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Set 'Order Date' as index for the DataFrame
df = data.set_index('Order Date')

# Visualize sales trend over time using a line plot
plt.plot(df.index, df['Sales'], label='Sales')
plt.xlabel('Order Date')
plt.ylabel('Sales')
plt.title('Time Series Analysis: Sales Trend Over Time')
plt.legend()
plt.show()

# Perform statistical analysis on the time-series data (e.g., autocorrelation, stationarity testing)
from statsmodels.tsa.stattools import adfuller, acf

# Check for stationarity using Augmented Dickey-Fuller test
result = adfuller(df['Sales'])
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
if result[1] > 0.05:
    print("Data is non-stationary")
else:
    print("Data is stationary")

# Plot autocorrelation function for Sales
plt.plot(range(len(df['Sales'])), acf(df['Sales'], nlags=10))
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Autocorrelation Function of Sales')
plt.show()

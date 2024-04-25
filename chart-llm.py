import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('dataorders-withnull.csv')

# Group data by Customer Segment and sum Unit Price
grouped = data.groupby('Customer Segment')['Unit Price'].sum().reset_index(name='TotalUnitPrice')

# Create a bar chart
plt.bar(x=grouped['Customer Segment'], height=grouped['TotalUnitPrice'])
plt.xlabel('Customer Segment')
plt.ylabel('Sum of Unit Price')
plt.title('Sum of Unit Price by Customer Segment')
plt.show()
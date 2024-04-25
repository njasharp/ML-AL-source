
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('dataorders-withnull.csv')

# Group data by Product Category and sum Sales
grouped = data.groupby('Product Category')['Sales'].sum().reset_index(name='TotalSales')

# Create a bar chart
plt.bar(x=grouped['Product Category'], height=grouped['TotalSales'])
plt.xlabel('Product Category')
plt.ylabel('Sum of Sales')
plt.title('Sum of Sales by Product Category')
plt.show()

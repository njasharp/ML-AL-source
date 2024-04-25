import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('dataorders-withnull.csv')

# Calculate Profit (Profit = Sales) for each record in the DataFrame
data['Profit'] = data['Sales']

# Group data by Product Category and calculate average Profit Margin for each category
profit_by_category = data.groupby('Product Category')['Profit'].mean().reset_index(name='AvgProfitMargins')

# Create a bar chart to display profit margins by product categories
plt.bar(x=profit_by_category['Product Category'], height=profit_by_category['AvgProfitMargins'])
plt.xlabel('Product Category')
plt.ylabel('Average Profit Margin (Sales)')
plt.title('Profitability Analysis: Average Profit Margins by Product Category')
plt.show()

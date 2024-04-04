import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = np.random.randn(10)

# Sample x and y data
x = np.linspace(0, 10, len(data))
y_data = np.random.randn(len(x))
trend = np.polyval([1, -0.5], x)
mask = y_data > trend
data_above = y_data[mask]
data_below = y_data[~mask]
fig, axs = plt.subplots(ncols=2, figsize=(10, 5))

# Plot data points above the trend line
axs[0].plot(x, x[mask], 'o', label='Data Above')
axs[0].plot(x, trend, '-k', label='Trend Line')
axs[0].set_title('Data Above Trend Line')
axs[0].legend()

# Plot data points below the trend line
axs[1].plot(x, x[~mask], 'o', label='Data Below')
axs[1].plot(x, trend, '-k', label='Trend Line')
axs[1].set_title('Data Below Trend Line')
axs[1].legend()

plt.tight_layout()
plt.show()

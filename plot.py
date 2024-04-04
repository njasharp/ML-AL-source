import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.array([1, 2, 3, 4])
y = x * 2  # Y-axis values (twice the corresponding x-values)

# Create a basic line plot
plt.plot(x, y)

# Add labels and a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")

# Display the plot
plt.show()

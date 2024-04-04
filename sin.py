import matplotlib.pyplot as plt
import numpy as np

# Generate x values from 0 to 2*pi (one full cycle of sine wave)
x = np.linspace(0, 2 * np.pi, 1000)

# Calculate corresponding y values for the sine wave
y = np.sin(x)

# Create a basic line plot for the sine wave
plt.plot(x, y, label="Sine Wave", color="blue")

# Add labels and a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sine Wave Plot")

# Display the plot
plt.legend()  # Show the legend for the sine wave
plt.grid(True)  # Add grid lines
plt.show()

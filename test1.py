import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.randint(10, size=(50, 5))

plt.figure(figsize=(8,6))
sns.heatmap(data, cmap='coolwarm')

plt.title('Heatmap Example')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()

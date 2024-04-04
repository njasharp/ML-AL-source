import numpy
import matplotlib.pyplot as plt


y = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(y, 100)
plt.show()
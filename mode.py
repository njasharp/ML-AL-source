from scipy import stats
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print ("array", speed)
x = stats.mode(speed)

print(x)

x = numpy.mean(speed)

print("mean", x)

x = numpy.median(speed)

print("median", x)
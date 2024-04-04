import numpy

speed = [86,87,88,86,87,85,86]
speed2 = [32,111,138,28,59,77,97]

x = numpy.std(speed)
y= numpy.std(speed2)

print(speed, x)
print(speed2, y)
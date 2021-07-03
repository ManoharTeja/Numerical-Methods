# Example 5.2 in Chap 5 of Chapra
import math
import matplotlib.pyplot as plot

a = int(input("Enter the min value of the range between which the brackets are to be determined: "))
b = int(input("Enter the max value of the range between which the brackets are to be determined: "))
n = int((b - a)/0.01)
x = [1]*n
x[0] = a
y = [1]*n
y[0] = (math.sqrt(39.24 * x[0]) * math.tanh(4 * math.sqrt(2.4525/x[0]))) - 36
for i in range(1, n):
    x[i] = x[i-1] + 0.1
    y[i] = (math.sqrt(39.24 * x[i]) * math.tanh(4 * math.sqrt(2.4525/x[i]))) - 36
    if (y[i] * y[i-1]) < 0:
        print("Bracket is (", x[i-1], ", ", x[i], ")")

plot.plot(x, y)
plot.grid(True)
plot.show()

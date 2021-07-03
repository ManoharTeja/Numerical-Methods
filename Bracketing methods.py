# There are two popular bracketing methods to find the roots:
# i) Bisection method, ii) False-Position method

import math


# Bisection Method
def bisection():
    print("Result from Bisection method:")
    x = [1] * 100  # Create an array of 100 elements so that 98 further calculations can be done
    y = [1] * 100  # Create an array of 100 elements so that 98 further calculations can be done
    x[0] = float(input("Enter the lower guess(Make sure f(xl)<0, else program gives wrong answer): "))
    x[1] = float(input("Enter the upper guess(Make sure f(xl)>0, else program gives wrong answer): "))
    for i in range(2):
        (math.sqrt(39.24 * x[i]) * math.tanh(4 * math.sqrt(2.4525/x[i]))) - 36

    x[2] = (x[0] + x[1]) / 2
    for i in range(2, 99):
        y[i] = (math.sqrt(39.24 * x[i]) * math.tanh(4 * math.sqrt(2.4525/x[i]))) - 36  # Write the equation of function whose root is to be found
        if -0.0005 < y[i] < 0.0005:
            return x[i]
        else:
            if y[i] > 0:
                if y[i - 1] > 0:
                    x[i + 1] = (x[i] + x[i - 2]) / 2
                else:
                    x[i + 1] = (x[i - 1] + x[i]) / 2

            if y[i] < 0:
                if y[i - 1] < 0:
                    x[i + 1] = (x[i] + x[i - 2]) / 2
                else:
                    x[i + 1] = (x[i - 1] + x[i]) / 2


# False-Position method
def false_position():
    print("Result from False Position method:")
    x = [1] * 100  # Create an array of 100 elements so that 98 further calculations can be done
    y = [1] * 100  # Create an array of 100 elements so that 98 further calculations can be done
    x[0] = float(input("Enter the lower guess(Make sure f(xl)<0, else program gives wrong answer): "))
    x[1] = float(input("Enter the upper guess(Make sure f(xl)>0, else program gives wrong answer): "))
    for i in range(2):
        y[i] = (math.sqrt(39.24 * x[i]) * math.tanh(4 * math.sqrt(2.4525/x[i]))) - 36

    x[2] = x[1] - (y[1] * (x[0] - x[1])/(y[0] - y[1]))
    for i in range(2, 99):
        y[i] = (math.sqrt(39.24 * x[i]) * math.tanh(4 * math.sqrt(2.4525/x[i]))) - 36  # Write the equation of function whose root is to be found
        if -0.0005 < y[i] < 0.0005:
            return x[i]
        else:
            if y[i] > 0:
                if y[i - 1] > 0:
                    x[i + 1] = x[i] - (y[i] * (x[i-2] - x[i])/(y[i-2] - y[i]))
                else:
                    x[i + 1] = x[i] - (y[i] * (x[i] - x[i-1])/(y[i] - y[i-1]))

            if y[i] < 0:
                if y[i - 1] < 0:
                    x[i + 1] = x[i-2] - (y[i-2] * (x[i] - x[i-2])/(y[i] - y[i-2]))
                else:
                    x[i + 1] = x[i-2] - (y[i-2] * (x[i] - x[i-1])/(y[i] - y[i-1]))


x1 = bisection()
print("The root of the given function is ", x1)

x2 = false_position()
print("The root of the given function is ", x2)

error = (abs((x2 - x1))/round(x1)) * 100
print("The percentage error between the results from the two methods is ", error, "%")

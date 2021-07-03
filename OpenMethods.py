# Open Methods to find roots do not require two guess bracketing the root b/w them
# Simple Fixed Point Method, Newton Raphson, Secant Method are famous open methods
from math import *
from sympy import *


# Fixed Point Method.... Suppose that we wanted to find root of f(x),
# At root f(x) = 0, we modify f(x)=0 as x=g(x)
def fixed_point():
    print("Using Fixed Point Method to find root")
    x = [1] * 100  # Creating an array of 100 elements
    y = [1] * 100
    x[0] = float(input("Enter the guess: "))
    for i in range(1, 99):
        y[i-1] = (sqrt(39.24 * x[i-1]) * tanh(4 * sqrt(2.4525/x[i-1]))) - 36 + x[i-1]  # Enter g(x)
        if -0.005 < y[i - 1] < 0.005:  # Error tolerance +/-(0.5%)
            return x[i - 1]
        else:
            x[i] = y[i - 1]


def newton_raphson():
    print("Using Newton Raphson Method to find root")
    x1 = [1] * 100  # Creating an array of 100 elements
    y = [1] * 100
    ydiff = [1] * 100
    x1[0] = float(input("Enter the guess: "))

    x = symbols('x')
    expr = ((39.24 * x)**0.5 * tanh(4 * (2.4525/x)**0.5)) - 36
    expr_diff = Derivative(expr, x).doit()  # code f(x) in parenthesis

    for i in range(1, 99):
        y[i - 1] = (sqrt(39.24 * x1[i-1]) * tanh(4 * sqrt(2.4525/x1[i-1]))) - 36
        # Enter the function f(x) whose root is to be determined
        if -0.005 < y[i - 1] < 0.005:
            return x1[i - 1]
        else:
            ydiff[i - 1] = expr_diff.subs({x: x1[i - 1]}).doit()
            x1[i] = x1[i - 1] - (y[i - 1] / ydiff[i - 1])


def secant():
    print("Using Secant Method to find root")
    x = [1] * 100  # Creating an array of 100 elements
    x[0] = float(input("Enter the guess1: "))
    x[1] = float(input("Enter the guess2: "))
    y = [1] * 100
    for i in range(0, 2):
        y[i] = (sqrt(39.24 * x[i]) * tanh(4 * sqrt(2.4525/x[i]))) - 36  # Enter the function f(x) whose root is to be determined
    print(" ", y)
    for i in range(2, 99):
        if -0.005 < y[i - 1] < 0.005:
            return x[i - 1]
        else:
            x[i] = x[i - 1] - (y[i - 1] * ((x[i - 1] - x[i - 2]) / (y[i - 1] - y[i - 2])))
            y[i] = (sqrt(39.24 * x[i]) * tanh(4 * sqrt(2.4525/x[i]))) - 36  # Enter the function f(x) whose root is to be determined


alpha = fixed_point()
print("The root of the function is ", alpha)


beta = newton_raphson()
print("The root of the function is ", beta)


gamma = secant()
print("The root of the function is ", gamma)

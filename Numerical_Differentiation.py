from math import *


# Euler method/ RK First order method dy/dt = f(t,y) => y(i+1) = y(i) + f(t,y)(dt)
def euler_method():
    ti = 0  # float(input("Enter the initial time: "))
    tf = 4  # float(input("Enter the final time: "))
    dt = 1  # float(input("Enter the time step: "))
    n = int((tf - ti)/dt)
    t = [1] * int(n+1)
    t[0] = ti
    t[n] = tf
    for i in range(n):
        t[i+1] = t[i] + dt

    y = [1] * int(n+1)
    y[0] = 2    # initial condition given from IVP
    for i in range(n):
        y[i+1] = y[i] + (((4 * exp(0.8 * t[i])) - (0.5 * y[i])) * dt)  # ... => enter the function f(t,y)
    return y


# Heun's Method(without iteration) or RK second order method with a2 = 1/2
def heun_method():
    ti = 0  # float(input("Enter the initial time: "))
    tf = 4  # float(input("Enter the final time: "))
    dt = 1  # float(input("Enter the time step: "))
    n = int((tf - ti) / dt)
    t = [1] * int(n + 1)
    t[0] = ti
    t[n] = tf
    for i in range(n):
        t[i + 1] = t[i] + dt

    y = [1] * (n + 1)
    y[0] = 2  # initial condition given from IVP
    dydt = [1] * (n+1)
    for i in range(n):
        dydt[i] = ((4 * exp(0.8 * t[i])) - (0.5 * y[i]))    # ... => enter the function f(t,y)
        y[i+1] = y[i] + (dydt[i] * dt)
        dydt[i+1] = ((4 * exp(0.8 * t[i+1])) - (0.5 * y[i+1]))
        y[i+1] = y[i] + (((dydt[i] + dydt[i+1]) / 2) * dt)
    return y


# Midpoint Method or RK second order method with a2 = 1
def midpoint_method():
    ti = 0  # float(input("Enter the initial time: "))
    tf = 4  # float(input("Enter the final time: "))
    dt = 1  # float(input("Enter the time step: "))
    n = int((tf - ti) / dt)
    t = [1] * int((2 * n) + 1)
    t[0] = ti
    t[(2 * n)] = tf
    for i in range(2*n):
        t[i+1] = t[i] + (dt/2)
    y = [1] * int((2 * n) + 1)
    y[0] = 2  # initial condition given from IVP
    dydt = [1] * int((2 * n) + 1)
    sol = [1] * (n+1)
    sol[0] = y[0]
    for i in range(0, (2 * n)-1, 2):
        dydt[i] = ((4 * exp(0.8 * t[i])) - (0.5 * y[i]))    # ... => enter the function f(t,y)
        y[i+1] = y[i] + (dydt[i] * (dt/2))
        dydt[i+1] = ((4 * exp(0.8 * t[i+1])) - (0.5 * y[i+1]))
        y[i+2] = y[i] + (dydt[i+1] * dt)
        j = int(i/2)
        sol[j+1] = y[i+2]
    return sol


# Ralston's Method or RK second order method with a2 = 3/4
def ralston_method():
    ti = 0  # float(input("Enter the initial time: "))
    tf = 4  # float(input("Enter the final time: "))
    dt = 1  # float(input("Enter the time step: "))
    n = int((tf - ti) / dt)
    t = [1] * (n + 1)
    t[0] = ti
    t[n] = tf
    for i in range(n):
        t[i + 1] = t[i] + dt

    y = [1] * (n + 1)
    y[0] = 2  # initial condition given from IVP
    dydt = [1] * (n+1)
    for i in range(n):
        k1 = ((4 * exp(0.8 * t[i])) - (0.5 * y[i])) # k1 is just dydt(yi, ti)
        k2 = ((4 * exp(0.8 * (t[i] + ((2*dt)/3)))) - (0.5 * (y[i] + ((2*k1*dt)/3))))
        y[i+1] = y[i] + (((k1/4)+((3*k2)/4)) * dt)
        dydt[i+1] = ((4 * exp(0.8 * t[i + 1])) - (0.5 * y[i + 1]))
        y[i+1] = y[i] + (((dydt[i] + dydt[i + 1]) / 2) * dt)
    return y


# RK4 Method
def rk4():
    ti = 0  # float(input("Enter the initial time: "))
    tf = 4  # float(input("Enter the final time: "))
    dt = 1  # float(input("Enter the time step: "))
    n = int((tf - ti) / dt)
    t = [1] * (n + 1)
    t[0] = ti
    t[n] = tf
    for i in range(n):
        t[i + 1] = t[i] + dt

    y = [1] * (n + 1)
    y[0] = 2  # initial condition given from IVP
    for i in range(n):
        k1 = ((4 * exp(0.8 * t[i])) - (0.5 * y[i]))     # k1 is just dydt(yi, ti)
        k2 = ((4 * exp(0.8 * (t[i]+(dt/2)))) - (0.5 * (y[i] + ((k1*dt)/2))))
        k3 = ((4 * exp(0.8 * (t[i]+(dt/2)))) - (0.5 * (y[i] + ((k2*dt)/2))))
        k4 = ((4 * exp(0.8 * (t[i]+dt))) - (0.5 * (y[i] + (k3*dt))))
        y[i+1] = y[i] + (((k1 + (2*k2) + (2*k3) + k4)*dt)/6)
    return y


y = euler_method()
print("The values of y at time t = [0, 1, 2, 3, 4] is ", y)

y = heun_method()
print("The values of y at time t = [0, 1, 2, 3, 4] is ", y)

y = midpoint_method()
print("The values of y at time t = [0, 1, 2, 3, 4] is ", y)


y = ralston_method()
print("The values of y at time t = [0, 1, 2, 3, 4] is ", y)


y = rk4()
print("The values of y at time t = [0, 1, 2, 3, 4] is ", y)

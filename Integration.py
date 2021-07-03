# Trapezoidal rule is used to integrate a function numerically between a certain limits
def trapezoidal():
    print("Using the Trapezoidal rule")
    x = [1] * 2
    y = [1] * 2
    x[0] = float(input("Enter the lower limit of integration: "))
    x[1] = float(input("Enter the upper limit of integration: "))
    for i in range(0, 1):
        y[i] = 0.2 + (25 * x[i]) - (200 * x[i]**2) + (675 * x[i]**3) - (900 * x[i]**4) + (400 * x[i]**5)  # Enter the integration function

    trap = (x[1] - x[0]) * ((y[1] + y[0])/2)
    return trap


def composite_trapezoidal():
    print("Using the Composite Trapezoidal rule")
    n = int(input("Enter the number of divisions to be made: "))
    x = [1] * (n + 1)
    y = [1] * (n + 1)
    x[0] = float(input("Enter the lower limit of integration: "))
    x[n] = float(input("Enter the upper limit of integration: "))
    h = (x[n] - x[0])/n
    print("Your step size is ", h)
    for i in range(1, n+1):   # i goes from 1 to n, not n+1
        x[i] = x[i-1] + h
    print("\n ", x)
    for i in range(0, n+1):     # i goes from 0 to n
        y[i] = 0.2 + (25 * x[i]) - (200 * x[i]**2) + (675 * x[i]**3) - (900 * x[i]**4) + (400 * x[i]**5)  # Enter the integration function
    print("\n ", y)
    comp_trap = 0
    for i in range(0, n+1):
        if i == 0:
            comp_trap = comp_trap + y[i]
        elif 0 < i < n:
            comp_trap = comp_trap + (2 * y[i])
        else:
            comp_trap = comp_trap + y[i]
    comp_trap = comp_trap * (h / 2)
    return comp_trap


def simpson_onethird():
    print("Using the Simpson One-Third rule")
    x = [1] * 3
    y = [1] * 3
    x[0] = float(input("Enter the lower limit of integration: "))
    x[2] = float(input("Enter the upper limit of integration: "))
    x[1] = (x[0] + x[2])/2
    for i in range(0, 3):   # i goes from 0 to 2
        y[i] = 0.2 + (25 * x[i]) - (200 * x[i]**2) + (675 * x[i]**3) - (900 * x[i]**4) + (400 * x[i]**5)  # Enter the integration function
    print("\n ", y)
    sim_13 = ((x[2] - x[0])/6) * (y[0] + (4 * y[1]) + y[2])
    return sim_13


def composite_simpson_onethird():
    print("Using the Composite Simpson One-Third rule")
    n = 4   # int(input("Enter the number of divisions to be made (must be an even number): "))
    x = [1] * (n + 1)
    y = [1] * (n + 1)
    print("\n ", x, y)
    x[0] = 0    # float(input("Enter the lower limit of integration: "))
    x[n] = 0.8  # float(input("Enter the upper limit of integration: "))
    h = (x[n] - x[0])/n
    print("Your step size is ", h)
    for i in range(1, n+1):
        x[i] = x[i-1] + h
    print("\n ", x)
    for i in range(0, n+1):
        y[i] = 0.2 + (25 * x[i]) - (200 * x[i]**2) + (675 * x[i]**3) - (900 * x[i]**4) + (400 * x[i]**5)  # Enter the integration function
    print("\n ", y)
    comp_sim13 = 0
    for i in range(0, n+1):
        if i == 0:
            comp_sim13 = comp_sim13 + y[i]
        elif i == n:
            comp_sim13 = comp_sim13 + y[i]
        elif i % 2 == 1:
            comp_sim13 = comp_sim13 + (4 * y[i])
        elif i % 2 == 0:
            comp_sim13 = comp_sim13 + (2 * y[i])
        print("\n ", comp_sim13)
    comp_sim13 = comp_sim13 * (h / 3)
    return comp_sim13


def simpson_threeeighth():
    print("Using the Simpson Three-Eighth rule")
    x = [1] * 4
    y = [1] * 4
    x[0] = float(input("Enter the lower limit of integration: "))
    x[3] = float(input("Enter the upper limit of integration: "))
    h = (x[3] - x[0])/3
    for i in range(1, 3):
        x[i] = x[i-1] + h
    print(" ", x)
    for i in range(0, 4):
        y[i] = 0.2 + (25 * x[i]) - (200 * x[i]**2) + (675 * x[i]**3) - (900 * x[i]**4) + (400 * x[i]**5)  # Enter the integration function
    print(" ", y)
    sim_38 = ((3 * h)/8) * (y[0] + (3 * y[1]) + (3 * y[2]) + y[3])
    return sim_38


def unequal_spacing():
    x = [0, 0.12, 0.22, 0.32, 0.36, 0.40, 0.44, 0.54, 0.64, 0.70, 0.80]
    n = len(x)
    print(" ", n)
    y = [1]*n
    h = [1]*(n-1)
    for i in range(n):
        y[i] = 0.2 + (25 * x[i]) - (200 * x[i]**2) + (675 * x[i]**3) - (900 * x[i]**4) + (400 * x[i]**5)
    print(" ", y)
    for i in range(n-1):  # i = [0, n-1]
        h[i] = x[i+1] - x[i]
    print(" ", h)
    ans = 0
    for i in range(n-1):
        ans = ans + h[i] * ((y[i] + y[i+1]) / 2)
        print(" ", ans)
    return ans


#sol1 = trapezoidal()
#print("The value of definite integration of function between the said limits is ", sol1)


#sol2 = composite_trapezoidal()
#print("The value of definite integration of function between the said limits is ", sol2)


#sol3 = simpson_onethird()
#print("The value of definite integration of function between the said limits is ", sol3)


#sol4 = composite_simpson_onethird()
#print("The value of definite integration of function between the said limits is ", sol4)


#sol5 = simpson_threeeighth()
#print("The value of definite integration of function between the said limits is ", sol5)


sol6 = unequal_spacing()
print("The value of definite integration of function between the said limits is ", sol6)

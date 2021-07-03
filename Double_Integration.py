# Double integration or two dimensional integration

def double_integration():
    Lx = 8  # int(input("Enter the length along x: "))
    nx = 4  # int(input("Enter the number of divisions along x: "))
    dx = Lx/nx  # hx = dx
    x = [1] * (nx+1)
    x[0] = 0
    for i in range(1, nx+1):
        x[i] = x[i-1] + dx

    Ly = 6  # int(input("Enter the length along y: "))
    ny = 3  # int(input("Enter the number of divisions along y: "))
    dy = Ly/ny  # hy = dy
    y = [1]*(ny+1)
    y[0] = 0
    for j in range(1, ny+1):
        y[j] = y[j-1] + dy

    T = [[1] * (nx+1)] * (ny+1)
    print(" ", T)
    print("Rows = ", len(T), "columns = ", len(T[0]))

    for j in range(1):
        for i in range(nx-1):
            T[i][j] = (2 * x[i] * y[j]) + (2 * x[i]) - pow(x[i], 2) - (2 * pow(y[j], 2)) + 72.0
            print(" ", i, j, T[i][j])
    print(" ", T)

    avg_temp = [1]*(ny + 1)
    #print(" ", avg_temp)
    temp = 0

    for j in range(nx+1):
        for i in range(0, nx + 1):
            if i == 0:
                avg_temp[j] = avg_temp[j] + T[i][j]
            elif i == nx:
                avg_temp[j] = avg_temp[j] + T[i][j]
            elif i % 2 == 1:
                avg_temp[j] = avg_temp[j] + (4 * T[i][j])
            elif i % 2 == 0:
                avg_temp[j] = avg_temp[j] + (2 * T[i][j])
        avg_temp[j] = avg_temp[j] * (dx / 3)
        if j == 0:
            temp = avg_temp[j]
        elif j == nx:
            temp = avg_temp[j]
        elif j % 2 == 1:
            temp = (4 * avg_temp[j])
        elif j % 2 == 0:
            temp = (2 * avg_temp[j])
    temp = temp * (dy / 3)
    return temp


average_temperature = double_integration()
#print("The average temperature is ", average_temperature)

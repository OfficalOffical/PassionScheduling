


def reqTime(x):
    temp = 0
    for i in range(len(x)):
        temp += x[i]
    return temp


def findShortest(x, y):
    temp = 100000

    shortest = -1

    if (x[0] == 0 and y[0] != 0):
        if (y[0] < temp):
            temp = y[0]
            shortest = 0
    else:
        if (x[0] > 0):
            x[0] -= 1

    if (x[1] == 0 and y[1] != 0):
        if (y[1] < temp):
            temp = y[1]
            shortest = 1
    else:
        if(x[1]>0):
            x[1] -= 1

    if (x[2] == 0 and y[2] != 0):
        if (y[2] < temp):
            temp = y[2]
            shortest = 2
    else:
        if (x[2] > 0):
            x[2] -= 1

    return shortest

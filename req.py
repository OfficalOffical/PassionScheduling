import schedule
from numpy import random

def reqTime(x):
    temp = 0
    for i in range(len(x)):
        temp += x[i]
    return temp


def findShortest(x, y):
    temp = 100000

    shortest = -1

    for i in range(len(x)):
        if(x[i] == 0 and y[i] != 0):
            if (y[i] < temp):
                temp = y[i]
                shortest = i
        else:
            if (x[i] > 0):
                    x[i] -= 1
    return shortest
"""
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
"""



import req
from numpy import random

# Turnaround time = Exit time - Arrival time
# Turnaround time = Burst time + Waiting time
# Waiting time = Turnaround time - Burst time
# Througput = waiting time /3


class process:
    def __init__(self, ID, start, end, ):
        self.ID = ID
        self.start = start
        self.end = end


def MLFQ():

    x1 = random.poisson(lam=2, size=10)
    y1 = random.poisson(lam=10, size=10)


    tempY1 = req.reqTime(y1)
    global pList
    global idleTime
    idleTime = 0

    pList = []
    for i in range(len(x1)):
        pList.append(process(i,-1,-1))



    t1,tempY = highPriority(x1, y1, (tempY1 * 0.5))  # SJF  hoca hepsine ayrı time derse buraya tempx
    t2,tempY = medPriority(tempY, (temp * 0.3), (temp * 0.5))  # buraya da x yerine tempX yaz
    t3,tempY = lowPriority(tempY, (temp * 0.8))
    printLast(temp,t1,t2,t3)

def highPriority(x, y, ratio):  # SJF
    # May i put waiting time to other scheduling algo's
    global idleTime
    tempX = x
    tempY = y
    for i in range(int(ratio)):
        temp = req.findShortest(tempX, tempY)
        if (temp != -1):
            tempY[temp] -= 1
            checkStartEnd(i, temp, tempY[temp])
        else:
            idleTime += 1
    return range(int(ratio)),tempY  # Buraya temp X ekleyebilirsin


def medPriority(tempY, ratio, realTime):
    realTime = int(realTime)
    ratio = int(ratio)
    time = 0
    temp = 0
    while True:
        if ((tempY[temp] / 4) > 1.0):  # Az beynini zorlasan olcak sanki
            for i in range(4):
                if (time == ratio):
                    break;
                else:
                    if ((tempY[temp] - 1) == 0):
                        checkStartEnd((realTime + time), temp, 0)
                    checkStartEnd((realTime + time), temp, -1)
                    tempY[temp] -= 1
                    time += 1

        else:
            for i in range(tempY[temp]):
                if (time == ratio):
                    break
                else:
                    if ((tempY[temp] - 1) == 0):
                        checkStartEnd((realTime + time), temp, 0)
                    checkStartEnd((realTime + time), temp, -1)
                    tempY[temp] -= 1
                    time += 1

        temp = ((temp + 1) % len(pList))
        if (time == ratio):
            break

    return time,tempY


def lowPriority(y, realTime):
    realTime = int(realTime)
    time = 0
    temp = 0
    p = pList
    while True:
        while True:
            if (y[temp] == 0):
                break
            if ((y[temp] - 1) == 0):
                checkStartEnd((realTime + time), temp, 0)
                y[temp] -= 1
                time += 1
                break
            else:
                checkStartEnd((realTime + time), temp, -1)
                y[temp] -= 1
                time += 1
        temp = ((temp + 1) % len(pList))
        if (endCheck()):
            break
    return time,y


def checkStartEnd(time, ID, var):
    for p in pList:
        if (p.ID == ID):
            if (p.start == -1):
                p.start = time
            elif (p.end == -1 and var == 0):
                p.end = (time + 1)

def endCheck():
    for obj in pList:
        if(obj.end == -1):
            return False
    return True

def printLast(globalTime,t1,t2,t3):
    for obj in pList:
        print("P", obj.ID, "-> Waiting Time :", obj.start, "Turn Around Time :", (obj.end - obj.start), )
    #for obj in pList:
        #print(obj.ID, obj.start, obj.end, sep=' ')



"""
Arrival Time: Time at which the process arrives in the ready queue.
Completion Time: Time at which process completes its execution.
Burst Time: Time required by a process for CPU execution.
Turn Around Time: Time Difference between completion time and arrival time.
Turn Around Time = Completion Time – Arrival Time

Waiting Time(W.T): Time Difference between turn around time and burst time.
Waiting Time = Turn Around Time – Burst Time
"""

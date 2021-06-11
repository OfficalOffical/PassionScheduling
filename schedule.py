import req
from numpy import random

# Turnaround time = Exit time - Arrival time
# Turnaround time = Burst time + Waiting time
# Waiting time = Turnaround time - Burst time
# Througput = waiting time /3


class process:
    def __init__(self, ID, start, end):
        self.ID = ID
        self.start = start
        self.end = end


def MLFQ():

    x1,y1,x2,y2,x3,y3,timeSum = init(lamX=4,lamY=4,lamZ=4)

    t1 = highPriority(x1, y1, (timeSum * 0.5))  # SJF  hoca hepsine ayrı time derse buraya tempx
    t2 = medPriority(y2, (timeSum * 0.3), (timeSum * 0.5))  # buraya da x yerine tempX yaz
    t3 = lowPriority(y3, (timeSum * 0.8))

    printLast(timeSum,t1,t2,t3)

def highPriority(x, y, ratio):  # SJF
    # May i put waiting time to other scheduling algo's
    global idleTime
    ratio = int(ratio)
    print(ratio)
    tempX = x
    tempY = y
    print(tempX,tempY)
    for i in range(ratio):
        temp = req.findShortest(tempX, tempY)
        if (temp != -1):
            tempY[temp] -= 1
            checkStartEndHigh(i, temp, tempY[temp])
        else:
            idleTime += 1

    return range(int(ratio))  # Buraya temp X ekleyebilirsin


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
                        checkStartEndMed((realTime + time), temp, 0)
                    checkStartEndMed((realTime + time), temp, -1)
                    tempY[temp] -= 1
                    time += 1

        else:
            for i in range(tempY[temp]):
                if (time == ratio):
                    break
                else:
                    if ((tempY[temp] - 1) == 0):
                        checkStartEndMed((realTime + time), temp, 0)
                    checkStartEndMed((realTime + time), temp, -1)
                    tempY[temp] -= 1
                    time += 1

        temp = ((temp + 1) % len(pList))
        if (time == ratio):
            break

    return time


def lowPriority(y, realTime):
    realTime = int(realTime)
    time = 0
    temp = 0
    while True:
        while True:
            if (y[temp] == 0):
                break
            if ((y[temp] - 1) == 0):
                checkStartEndLow((realTime + time), temp, 0)
                y[temp] -= 1
                time += 1
                break
            else:
                checkStartEndLow((realTime + time), temp, -1)
                y[temp] -= 1
                time += 1
        temp = ((temp + 1) % len(pList3))
        if (endCheck()):
            break
    return time


def checkStartEndHigh(time, ID, var):
    for p in pList:
        if (p.ID == ID):
            if (p.start == -1):
                p.start = time
            elif (p.end == -1 and var == 0):
                p.end = (time + 1)



def checkStartEndMed(time, ID, var):
    for p in pList2:
        if (p.ID == ID):
            if(var == 0):
                print("-> P : ", p.ID, ":", p.start, "Time : ", p.end, "Var :", var)
            if (p.start == -1):
                p.start = time
                print("Start : P : ", p.ID, ":", p.start, "Time : ", p.end)
            elif (p.end == -1 and var == 0):
                p.end = (time + 1)




def checkStartEndLow(time, ID, var):
    for p in pList3:
        if (p.ID == ID):
            if (p.start == -1):
                p.start = time
            elif (p.end == -1 and var == 0):
                p.end = (time + 1)


def endCheck():
    for obj in pList3:
        if(obj.end == -1):
            return False
    return True

def printLast(globalTime,t1,t2,t3):
    for obj in pList:
        print("High P", obj.ID, "-> Waiting Time :", obj.start, "Turn Around Time :", (obj.end - obj.start), )
    print("/////////////////////////////////////////////////")
    for obj in pList2:
        print("Med P", obj.ID, "-> Waiting Time :", obj.start, "Turn Around Time :", (obj.end - obj.start), )
    print("/////////////////////////////////////////////////")
    for obj in pList3:
        print("Low P", obj.ID, "-> Waiting Time :", obj.start, "Turn Around Time :", (obj.end - obj.start), )
    #for obj in pList:
        #print(obj.ID, obj.start, obj.end, sep=' ')

def init(lamX,lamY,lamZ):
    x1 = random.poisson(lam=lamX, size=10)
    y1 = random.poisson(lam=10, size=10)
    x2 = random.poisson(lam=lamY, size=10)
    y2 = random.poisson(lam=10, size=10)
    x3 = random.poisson(lam=lamZ, size=10)
    y3 = random.poisson(lam=10, size=10)



    timeSum = req.reqTime(y1)
    timeSum += req.reqTime(y2)
    timeSum += req.reqTime(y3)
    print("MasterClock : ", timeSum)

    global pList
    global pList2
    global pList3
    global idleTime

    idleTime = 0
    pList = []
    pList2 = []
    pList3 = []

    for i in range(len(x1)):
        pList.append(process(i,-1,-1))
    for i in range(len(x2)):
        pList2.append(process(i,-1,-1))
    for i in range(len(x3)):
        pList3.append(process(i,-1,-1))

    return x1,y1,x2,y2,x3,y3,timeSum


"""
Arrival Time: Time at which the process arrives in the ready queue.
Completion Time: Time at which process completes its execution.
Burst Time: Time required by a process for CPU execution.
Turn Around Time: Time Difference between completion time and arrival time.
Turn Around Time = Completion Time – Arrival Time

Waiting Time(W.T): Time Difference between turn around time and burst time.
Waiting Time = Turn Around Time – Burst Time
"""

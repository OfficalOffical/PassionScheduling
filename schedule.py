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

    runAndOptimize(10)



def highPriority(x, y, ratio):  # SJF
    ratio = int(ratio)
    global idleTime
    idleTime = 0
    tempX = x
    tempY = y
    for i in range(ratio):
        temp = req.findShortest(tempX, tempY)
        if (temp != -1):
            tempY[temp] -= 1
            checkStartEndHigh(i, temp, tempY[temp])
        else:
            idleTime += 1

    if (idleTime <= 3):
        idleTime = 0
    return idleTime  # Buraya temp X ekleyebilirsin


def medPriority(tempY, ratio):
    ratio = int(ratio)
    global idleMed
    idleMed = 0
    time = 0
    temp = 0
    while True:
        if ((tempY[temp] / 4) >= 1.0):  # Az beynini zorlasan olcak sanki
            for i in range(4):
                if (time >= ratio):
                    break;
                else:
                    if ((tempY[temp] - 1) == 0):
                        checkStartEndMed((time), temp, 0)
                    checkStartEndMed((time), temp, -1)
                    tempY[temp] -= 1
                    time += 1

    #inf verirsen düzelebilir
        else:
            for i in range(tempY[temp]):
                if (time >= ratio):
                    break
                else:
                    if ((tempY[temp] - 1) == 0):
                        checkStartEndMed((time), temp, 0)
                    checkStartEndMed((time), temp, -1)
                    tempY[temp] -= 1
                    time += 1
        temp = ((temp + 1) % len(pList2))
        if (time >= ratio):
            break
        if(endCheckMed()):
            idleMed += 1
            time += 1
    return idleMed


def lowPriority(tempY,ratio):
    y = tempY
    global  idleLow
    idleLow = 0
    time = 0
    temp = 0
    while True:
        while True:
            if (y[temp] == 0):
                break
            if ((y[temp] - 1) == 0):
                checkStartEndLow((time), temp, 0)
                y[temp] -= 1
                time += 1
                break
            else:
                checkStartEndLow((time), temp, -1)
                tempY[temp] -= 1
                time += 1
        temp = ((temp + 1) % len(pList3))
        if ((time >= ratio)):
            break
        if(endCheck()):
            time += 1
            idleLow += 1
    return idleLow


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
            if (p.start == -1):
                p.start = time
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
    waitHigh = 0
    avTurnHigh = 0
    waitMed = 0
    avTurnMed = 0
    waitLow = 0
    avTurnLow = 0
    for obj in pList:
        if (obj.end == -1):
            print( "High P", obj.ID, " doesnt finished" )
        else:
            waitHigh += obj.start
            avTurnHigh += (obj.end - obj.start)
            print( "High P", obj.ID, "-> Waiting Time :",obj.start,"Turn Around Time :", (obj.end - obj.start), )

    print("/////////////////////////////////////////////////")
    for obj in pList2:
        if (obj.end == -1):
            print( "Med P", obj.ID, " doesnt finished" )
        else:
            waitMed += obj.start
            avTurnMed += (obj.end - obj.start)
            print( "Med P", obj.ID, "-> Waiting Time :", obj.start, "Turn Around Time :", (obj.end - obj.start), )

    print("/////////////////////////////////////////////////")
    for obj in pList3:
        if (obj.end == -1):
            print( "Low P", obj.ID, " doesnt finished" )
        else:
            waitLow += obj.start
            avTurnLow += (obj.end - obj.start)
            print( "Low P", obj.ID, "-> Waiting Time :", obj.start, "Turn Around Time :", (obj.end - obj.start), )

    print( "P1-> Average waiting time : ", (waitHigh / len( pList )), "Utilization Time : ",
           int(((tempTimeX - idleTime) / tempTimeX) * 100), " Throughput", tpAl( 1 ), "Average Turnaround time :",
           avTurnHigh, "Idle time : ", t1, "Average Lenght : ", tempTimeX )
    print( "P2-> Average waiting time : ", (waitMed / len( pList2 )), "Utilization Time : ",
           int(((tempTimeY - idleMed) / tempTimeY) * 100), " Throughput", tpAl( 2 ), "Average Turnaround time :",
           avTurnMed, "Idle time : ", t2, "Average Lenght : ", tempTimeY )
    print( "P3-> Average waiting time : ", (waitLow / len( pList3 )), "Utilization Time : ",
           int(((tempTimeZ - idleLow) / tempTimeX) * 100), " Throughput", tpAl( 3 ), "Average Turnaround time :",
           avTurnLow, "Idle time : ", t3, "Average Lenght : ", tempTimeZ )


    # for obj in pList:
    # print(obj.ID, obj.start, obj.end, sep=' ')

    """
    Arrival Time: Time at which the process arrives in the ready queue.
    Completion Time: Time at which process completes its execution.
    Burst Time: Time required by a process for CPU execution.
    Turn Around Time: Time Difference between completion time and arrival time.
    Turn Around Time = Completion Time – Arrival Time

    Waiting Time(W.T): Time Difference between turn around time and burst time.
    Waiting Time = Turn Around Time – Burst Time
    """
def tpAl(priority):
    tempSum = 0
    counter = 0
    if(priority == 1):
        for obj in pList:
            if (obj.end != -1):
                tempSum += obj.end - obj.start
                counter += 1
    if (priority == 2):
        for obj in pList2:
            if (obj.end != -1):
                tempSum += obj.end - obj.start
                counter += 1
    if (priority == 3):
        for obj in pList3:
            if (obj.end != -1):
                tempSum += obj.end - obj.start
                counter += 1

    return int(tempSum/counter)





def init(lamX,lamY,lamZ):

    x1,y1,x2,y2,x3,y3 = generatePoisson(lamX,lamY,lamZ)

    global tempTimeX
    global tempTimeY
    global tempTimeZ

    tempTimeX = req.reqTime(y1)
    tempTimeY = req.reqTime(y2)
    tempTimeZ = req.reqTime(y3)

    timeSum = tempTimeX + tempTimeY + tempTimeZ

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


def generatePoisson(lamX,lamY,lamZ):
    sizeHigh = 10
    sizeMed = 10
    sizeLow = 10
    x1 = random.poisson( lam = lamX, size = sizeHigh )
    for x in range(len(x1)):
        while(x1[x] == 0):
            x1[x] = random.poisson( lam = lamX, size = 1 )
    y1 = random.poisson( lam = 10, size = sizeHigh )
    for x in range(len(y1)):
        while(y1[x] == 0):
            y1[x] = random.poisson( lam = lamX, size = 1 )
    x2 = random.poisson( lam = lamY, size = sizeMed )
    for x in range(len(x2)):
        while(x2[x] == 0):
            x2[x] = random.poisson( lam = lamY, size = 1 )
    y2 = random.poisson( lam = 10, size = sizeMed )
    for x in range(len(y2)):
        while(y2[x] == 0):
            y2[x] = random.poisson( lam = lamY, size = 1 )
    x3 = random.poisson( lam = lamZ, size = sizeLow )
    for x in range(len(x3)):
        while(x3[x] == 0):
            x3[x] = random.poisson( lam = lamZ, size = 1 )
    y3 = random.poisson( lam = 10, size = sizeLow )
    for x in range(len(y3)):
        while(y3[x] == 0):
            y3[x] = random.poisson( lam = lamZ, size = 1 )

    return x1,y1,x2,y2,x3,y3

def endCheckMed():
    for obj in pList2:
        if(obj.end == -1):
            return False
    return True

def runAndOptimize(runTime):
    runTime = runTime % 30
    highRatio = 0.5
    medRatio = 0.3
    lowRatio = 0.2
    for x in range(runTime):
        tempX1, tempY1, tempX2, tempY2, tempX3, tempY3, timeSum = init( 6, 7, 4 )
        acc = 0.02
        t1 = highPriority(tempX1, tempY1, (timeSum * highRatio))
        t2 = medPriority(tempY2, (timeSum * medRatio))
        t3 = lowPriority(tempY3, (timeSum * lowRatio))

        if(t1 > t2 and t1 > t3):
            if(t2 == 0 or t2 < t3):
                highRatio -=acc
                medRatio += acc
            else:
                highRatio -=acc
                lowRatio += acc
        elif(t2 > t3 and t2 > t1):
            if(t3 == 0 or t3 > t1):
                medRatio -= acc
                lowRatio += acc
            else:
                medRatio -= acc
                highRatio += acc
        else:
            print(t1,t2,t3)
            if(t1 == 0 or t1 > t2):
                lowRatio -= acc
                highRatio += acc
            else:
                lowRatio -= acc
                medRatio += acc
        printLast(timeSum,t1,t2,t3)


    return timeSum,t1,t2,t3


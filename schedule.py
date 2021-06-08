import req

"""
Arrival Time: Time at which the process arrives in the ready queue.
Completion Time: Time at which process completes its execution.
Burst Time: Time required by a process for CPU execution.
Turn Around Time: Time Difference between completion time and arrival time.
Turn Around Time = Completion Time – Arrival Time

Waiting Time(W.T): Time Difference between turn around time and burst time.
Waiting Time = Turn Around Time – Burst Time
"""





#Turnaround time = Exit time - Arrival time
#Turnaround time = Burst time + Waiting time
#Waiting time = Turnaround time - Burst time
#Througput = waiting time /3


class process:
    def __init__(self,ID, start, end,):
        self.ID = ID
        self.start = start
        self.end = end


def MLFQ(x,y):
    print(x)
    print(y)
    temp = req.reqTime(y)
    global pList
    pList = []
    pList.append(process(0, -1, -1))
    pList.append(process(1, -1, -1))
    pList.append(process(2, -1, -1))

    tempY = highPriority(x,y,(temp*0.5))#SJF  hoca hepsine ayrı time derse buraya tempx
    medPriority(x,tempY,(temp*0.3),5) # buraya da x yerine tempX yaz

    print("vololo2")
    printList()
    print("vololo2")


def highPriority(x, y, ratio):#SJF
    global idleTime #May i put waiting time to other scheduling algo's
    idleTime=0
    tempX = x
    tempY = y
    temp = 0
    for i in range(int(ratio)):
        temp = req.findShortest(tempX,tempY)
        if (temp != -1):
            tempY[temp] -=1
            checkStartEnd(i,temp,tempY[temp])

        else:
            idleTime += 1

    return tempX,tempY

def medPriority(x,tempY, ratio,q):
    for x in range(int(ratio)):
        if(x%q == 0)

def checkStartEnd(time,ID,var):
    for p in pList:
        if(p.ID == ID):
            if(p.start == -1):
                p.start = time
            elif(p.end == -1 and var == 0):
                p.end = (time+1)


def printList():
    for obj in pList:
        print(obj.ID, obj.start,obj.end, sep=' ')
